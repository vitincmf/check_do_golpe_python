import random

from database import get_connection, placeholder, fetchall


def listar_assuntos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, descricao
        FROM assuntos
        ORDER BY nome
    """)

    assuntos = fetchall(cursor)
    conn.close()

    return assuntos


def sortear_quiz_total(total_questoes=10):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            q.id,
            q.titulo,
            q.descricao,
            q.url_simulada,
            q.resposta_correta,
            q.explicacao,
            q.dica,
            q.pontos,
            a.nome AS assunto
        FROM questoes q
        JOIN assuntos a ON q.assunto_id = a.id
        WHERE q.ativo = 1
    """)

    questoes = fetchall(cursor)
    conn.close()

    random.shuffle(questoes)

    return questoes[:total_questoes]


def sortear_quiz_por_assunto(assunto_id, total_questoes=10):
    conn = get_connection()
    cursor = conn.cursor()
    p = placeholder()

    cursor.execute(f"""
        SELECT 
            q.id,
            q.titulo,
            q.descricao,
            q.url_simulada,
            q.resposta_correta,
            q.explicacao,
            q.dica,
            q.pontos,
            a.nome AS assunto
        FROM questoes q
        JOIN assuntos a ON q.assunto_id = a.id
        WHERE q.ativo = 1
        AND q.assunto_id = {p}
    """, (assunto_id,))

    questoes = fetchall(cursor)
    conn.close()

    random.shuffle(questoes)

    return questoes[:total_questoes]


def sortear_questoes_por_grupos(quantidade_por_assunto=2):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome
        FROM assuntos
        ORDER BY id
    """)

    assuntos = fetchall(cursor)
    todas_questoes = []
    p = placeholder()

    for assunto in assuntos:
        cursor.execute(f"""
            SELECT 
                q.id,
                q.titulo,
                q.descricao,
                q.url_simulada,
                q.resposta_correta,
                q.explicacao,
                q.dica,
                q.pontos,
                a.nome AS assunto
            FROM questoes q
            JOIN assuntos a ON q.assunto_id = a.id
            WHERE q.assunto_id = {p}
            AND q.ativo = 1
        """, (assunto["id"],))

        questoes = fetchall(cursor)
        random.shuffle(questoes)

        todas_questoes.extend(questoes[:quantidade_por_assunto])

    conn.close()

    random.shuffle(todas_questoes)

    return todas_questoes