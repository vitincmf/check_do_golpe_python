import os
import uuid

from flask import Flask, render_template, request, redirect, url_for, session, flash
from dotenv import load_dotenv

from database import create_database, get_connection, placeholder, fetchone, fetchall
from quiz_service import sortear_quiz_total, sortear_quiz_por_assunto
from auth_service import criar_usuario, autenticar_usuario
from estatisticas_service import (
    estatisticas_gerais,
    estatisticas_por_faixa_etaria,
    estatisticas_por_grupo_perfil,
    estatisticas_por_faixa_e_grupo,
    estatisticas_por_assunto,
    estatisticas_por_idade_e_assunto,
    questoes_mais_erradas,
)

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "check-do-golpe-secret-dev")


# =====================
# INICIALIZAÇÃO DO BANCO
# =====================

create_database()

from data.seed import seed_database
seed_database()

from data.questoes_seed import seed_questoes
seed_questoes()


@app.before_request
def garantir_visitante():
    if "visitante_id" not in session:
        session["visitante_id"] = str(uuid.uuid4())


@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM faixas_etarias ORDER BY id")
    faixas = fetchall(cursor)

    cursor.execute("SELECT * FROM grupos_perfil ORDER BY id")
    grupos = fetchall(cursor)

    cursor.execute("SELECT * FROM assuntos ORDER BY nome")
    assuntos = fetchall(cursor)

    conn.close()

    return render_template(
        "index.html",
        faixas=faixas,
        grupos=grupos,
        assuntos=assuntos,
        usuario=session.get("usuario_nome"),
    )


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM faixas_etarias ORDER BY id")
    faixas = fetchall(cursor)

    conn.close()

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        faixa_etaria_id = request.form.get("faixa_etaria_id")

        ok, msg = criar_usuario(nome, email, senha, faixa_etaria_id)
        flash(msg)

        if ok:
            return redirect(url_for("login"))

    return render_template("cadastro.html", faixas=faixas)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        usuario = autenticar_usuario(email, senha)

        if usuario:
            session["usuario_id"] = usuario["id"]
            session["usuario_nome"] = usuario["nome"]
            flash("Login realizado com sucesso.")
            return redirect(url_for("index"))

        flash("E-mail ou senha inválidos.")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("usuario_id", None)
    session.pop("usuario_nome", None)
    flash("Você saiu da conta.")
    return redirect(url_for("index"))


@app.route("/iniciar", methods=["POST"])
def iniciar():
    faixa_etaria_id = request.form.get("faixa_etaria_id")
    grupo_perfil_id = request.form.get("grupo_perfil_id")
    modo_quiz = request.form.get("modo_quiz")

    if not faixa_etaria_id:
        flash("Selecione uma faixa etária para iniciar.")
        return redirect(url_for("index"))

    if not grupo_perfil_id:
        flash("Selecione seu perfil de experiência para iniciar.")
        return redirect(url_for("index"))

    if not modo_quiz:
        flash("Selecione o tipo de quiz.")
        return redirect(url_for("index"))

    if modo_quiz == "misturado":
        questoes = sortear_quiz_total(total_questoes=10)
    else:
        questoes = sortear_quiz_por_assunto(modo_quiz, total_questoes=10)

    if len(questoes) < 5:
        flash("Este tipo de quiz precisa ter pelo menos 5 questões cadastradas.")
        return redirect(url_for("index"))

    ids_questoes = [q["id"] for q in questoes]

    conn = get_connection()
    cursor = conn.cursor()
    p = placeholder()

    if p == "%s":
        cursor.execute(
            f"""
            INSERT INTO tentativas (
                usuario_id,
                visitante_id,
                faixa_etaria_id,
                grupo_perfil_id,
                total_questoes,
                pontuacao_total,
                total_acertos,
                total_erros,
                finalizada
            )
            VALUES ({p}, {p}, {p}, {p}, {p}, 0, 0, 0, 0)
            RETURNING id
            """,
            (
                session.get("usuario_id"),
                session.get("visitante_id"),
                faixa_etaria_id,
                grupo_perfil_id,
                len(ids_questoes),
            ),
        )

        retorno = cursor.fetchone()
        tentativa_id = retorno["id"] if isinstance(retorno, dict) else retorno[0]

    else:
        cursor.execute(
            f"""
            INSERT INTO tentativas (
                usuario_id,
                visitante_id,
                faixa_etaria_id,
                grupo_perfil_id,
                total_questoes,
                pontuacao_total,
                total_acertos,
                total_erros,
                finalizada
            )
            VALUES ({p}, {p}, {p}, {p}, {p}, 0, 0, 0, 0)
            """,
            (
                session.get("usuario_id"),
                session.get("visitante_id"),
                faixa_etaria_id,
                grupo_perfil_id,
                len(ids_questoes),
            ),
        )

        tentativa_id = cursor.lastrowid

    conn.commit()
    conn.close()

    session["tentativa_id"] = tentativa_id
    session["questoes"] = ids_questoes
    session["indice_atual"] = 0
    session["modo_quiz"] = modo_quiz
    session.pop("feedback", None)

    return redirect(url_for("questao"))


@app.route("/questao")
def questao():
    if "tentativa_id" not in session:
        return redirect(url_for("index"))

    indice = session["indice_atual"]
    questoes = session["questoes"]

    if indice >= len(questoes):
        return redirect(url_for("resultado"))

    questao_id = questoes[indice]

    conn = get_connection()
    cursor = conn.cursor()
    p = placeholder()

    cursor.execute(
        f"""
        SELECT 
            q.*,
            a.nome AS assunto
        FROM questoes q
        JOIN assuntos a ON q.assunto_id = a.id
        WHERE q.id = {p}
        """,
        (questao_id,),
    )

    questao = fetchone(cursor)
    conn.close()

    return render_template(
        "questao.html",
        questao=questao,
        numero=indice + 1,
        total=len(questoes),
        usuario=session.get("usuario_nome"),
    )


@app.route("/responder", methods=["POST"])
def responder():
    tentativa_id = session.get("tentativa_id")
    questao_id = request.form.get("questao_id")
    resposta_usuario = request.form.get("resposta_usuario")
    usou_dica = int(request.form.get("usou_dica", 0))

    if not tentativa_id:
        return redirect(url_for("index"))

    conn = get_connection()
    cursor = conn.cursor()
    p = placeholder()

    cursor.execute(f"SELECT * FROM questoes WHERE id = {p}", (questao_id,))
    questao = fetchone(cursor)

    acertou = 1 if resposta_usuario == questao["resposta_correta"] else 0

    pontos = 0

    if acertou:
        pontos = questao["pontos"]

        if usou_dica:
            pontos = pontos // 2

    cursor.execute(
        f"""
        INSERT INTO respostas (
            tentativa_id,
            questao_id,
            resposta_usuario,
            acertou,
            usou_dica,
            pontos_obtidos
        )
        VALUES ({p}, {p}, {p}, {p}, {p}, {p})
        """,
        (
            tentativa_id,
            questao_id,
            resposta_usuario,
            acertou,
            usou_dica,
            pontos,
        ),
    )

    cursor.execute(
        f"""
        UPDATE tentativas
        SET 
            pontuacao_total = pontuacao_total + {p},
            total_acertos = total_acertos + {p},
            total_erros = total_erros + {p}
        WHERE id = {p}
        """,
        (
            pontos,
            acertou,
            0 if acertou else 1,
            tentativa_id,
        ),
    )

    conn.commit()
    conn.close()

    session["feedback"] = {
        "questao_id": int(questao_id),
        "resposta_usuario": resposta_usuario,
        "acertou": acertou,
        "pontos": pontos,
        "usou_dica": usou_dica,
    }

    return redirect(url_for("feedback"))


@app.route("/feedback")
def feedback():
    dados = session.get("feedback")

    if not dados:
        return redirect(url_for("questao"))

    conn = get_connection()
    cursor = conn.cursor()
    p = placeholder()

    cursor.execute(
        f"""
        SELECT 
            q.*,
            a.nome AS assunto
        FROM questoes q
        JOIN assuntos a ON q.assunto_id = a.id
        WHERE q.id = {p}
        """,
        (dados["questao_id"],),
    )

    questao = fetchone(cursor)

    tentativa_id = session.get("tentativa_id")
    cursor.execute(f"SELECT pontuacao_total, total_questoes FROM tentativas WHERE id = {p}", (tentativa_id,))
    tentativa = fetchone(cursor)
    conn.close()

    return render_template(
        "feedback.html",
        questao=questao,
        dados=dados,
        numero=session.get("indice_atual", 0) + 1,
        total=tentativa["total_questoes"] if tentativa else len(session.get("questoes", [])),
        pontuacao_atual=tentativa["pontuacao_total"] if tentativa else 0
    )


@app.route("/proxima")
def proxima():
    session["indice_atual"] += 1

    if session["indice_atual"] >= len(session["questoes"]):
        return redirect(url_for("resultado"))

    return redirect(url_for("questao"))


@app.route("/resultado")
def resultado():
    tentativa_id = session.get("tentativa_id")

    if not tentativa_id:
        return redirect(url_for("index"))

    conn = get_connection()
    cursor = conn.cursor()
    p = placeholder()

    cursor.execute(
        f"""
        SELECT 
            t.*,
            f.nome AS faixa_etaria,
            g.nome AS grupo_nome,
            g.perfil AS grupo_perfil
        FROM tentativas t
        JOIN faixas_etarias f ON t.faixa_etaria_id = f.id
        LEFT JOIN grupos_perfil g ON t.grupo_perfil_id = g.id
        WHERE t.id = {p}
        """,
        (tentativa_id,),
    )

    tentativa = fetchone(cursor)

    cursor.execute(
        f"""
        UPDATE tentativas
        SET finalizada = 1
        WHERE id = {p}
        """,
        (tentativa_id,),
    )

    conn.commit()
    conn.close()

    percentual = 0

    if tentativa["total_questoes"] > 0:
        percentual = round(
            (tentativa["total_acertos"] / tentativa["total_questoes"]) * 100,
            2,
        )

    return render_template(
        "resultado.html",
        tentativa=tentativa,
        percentual=percentual,
    )


@app.route("/estatisticas")
def estatisticas():
    gerais = estatisticas_gerais()
    por_faixa = estatisticas_por_faixa_etaria()
    por_grupo = estatisticas_por_grupo_perfil()
    por_faixa_grupo = estatisticas_por_faixa_e_grupo()
    por_assunto = estatisticas_por_assunto()
    por_idade_assunto = estatisticas_por_idade_e_assunto()
    mais_erradas = questoes_mais_erradas()

    return render_template(
        "estatisticas.html",
        gerais=gerais,
        por_faixa=por_faixa,
        por_grupo=por_grupo,
        por_faixa_grupo=por_faixa_grupo,
        por_assunto=por_assunto,
        por_idade_assunto=por_idade_assunto,
        mais_erradas=mais_erradas,
    )


@app.route("/reiniciar")
def reiniciar():
    session.pop("tentativa_id", None)
    session.pop("questoes", None)
    session.pop("indice_atual", None)
    session.pop("modo_quiz", None)
    session.pop("feedback", None)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
