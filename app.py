
from flask import Flask, render_template, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import json
from datetime import datetime
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
DB_PATH = APP_DIR / "check_do_golpe.db"

app = Flask(__name__)
app.secret_key = "troque-esta-chave-em-producao"

QUESTIONS = [
    {
        "id": 1,
        "store": "BRADESCO - Área do Cliente",
        "url": "https://bradco-bradesco.com.br",
        "type": "Golpe",
        "title": "Esse site é legítimo ou uma armadilha?",
        "product": "Página de login bancário",
        "price": "",
        "payment": "Solicita CPF, senha e dados sensíveis",
        "image": "🏦",
        "hint": "Observe se o endereço realmente pertence ao banco.",
        "signals": ["URL com typosquatting", "Imitação visual de marca", "Solicitação de dados sensíveis"],
        "explanation": "Apesar de parecer uma área bancária, a URL não corresponde ao domínio oficial. Golpistas usam nomes parecidos para capturar dados de acesso."
    },
    {
        "id": 2,
        "store": "magazineluizaoficial",
        "url": "https://magazineluiza_promocao-especial-shop.top",
        "type": "Golpe",
        "title": "Esta loja online é confiável ou é um golpe?",
        "product": "Ar Condicionado Split Inverter 9.000 BTUs",
        "price": "R$ 1.150,00",
        "payment": "5% OFF no PIX",
        "image": "❄️",
        "hint": "Compare domínio, preço e forma de pagamento.",
        "signals": ["Domínio suspeito", "Preço muito baixo", "Uso de urgência promocional"],
        "explanation": "O site tenta se passar por uma grande loja, mas usa domínio estranho e promoção agressiva. Esses elementos são comuns em e-commerces falsos."
    },
    {
        "id": 3,
        "store": "Amazon Brasil",
        "url": "https://www.amazon.com.br",
        "type": "Seguro",
        "title": "Este cenário parece seguro?",
        "product": "Echo Dot 5ª geração",
        "price": "R$ 379,00",
        "payment": "Cartão, boleto ou PIX",
        "image": "🔊",
        "hint": "Verifique domínio, reputação e opções de pagamento.",
        "signals": ["Domínio oficial", "Múltiplas formas de pagamento", "Informações consistentes"],
        "explanation": "O domínio é oficial e os dados de compra são coerentes. Mesmo assim, o usuário deve conferir sempre o endereço antes de inserir dados."
    },
    {
        "id": 4,
        "store": "Super Ofertas Tech",
        "url": "https://superofertas-tech.xyz",
        "type": "Golpe",
        "title": "Oferta real ou golpe?",
        "product": "iPhone 14 Pro Max",
        "price": "R$ 1.299,00",
        "payment": "Somente PIX",
        "image": "📱",
        "hint": "Desconfie de descontos incompatíveis com o mercado.",
        "signals": ["Preço irreal", "Domínio incomum", "Somente PIX"],
        "explanation": "Preço muito abaixo do mercado e pagamento apenas por PIX são fortes indicadores de golpe."
    },
    {
        "id": 5,
        "store": "Mercado Livre",
        "url": "https://www.mercadolivre.com.br",
        "type": "Seguro",
        "title": "O anúncio parece legítimo?",
        "product": "Notebook Lenovo IdeaPad",
        "price": "R$ 2.899,00",
        "payment": "Cartão, boleto ou Mercado Pago",
        "image": "💻",
        "hint": "Procure por domínio oficial e meios de pagamento reconhecidos.",
        "signals": ["Domínio oficial", "Checkout conhecido", "Preço plausível"],
        "explanation": "O cenário apresenta domínio oficial, preço plausível e meios de pagamento reconhecidos."
    },
    {
        "id": 6,
        "store": "Correios Rastreamento",
        "url": "https://correios-entrega-pendente.info",
        "type": "Golpe",
        "title": "Taxa pendente: é confiável?",
        "product": "Liberação de encomenda",
        "price": "R$ 8,90",
        "payment": "PIX imediato",
        "image": "📦",
        "hint": "Golpes costumam usar urgência e taxas pequenas.",
        "signals": ["Domínio não oficial", "Urgência artificial", "Cobrança via PIX"],
        "explanation": "O domínio não é oficial e há tentativa de pressionar o usuário com uma taxa pequena e urgente."
    },
    {
        "id": 7,
        "store": "Loja Oficial Samsung",
        "url": "https://www.samsung.com/br",
        "type": "Seguro",
        "title": "Esta página é segura ou golpe?",
        "product": "Smartphone Galaxy",
        "price": "R$ 2.199,00",
        "payment": "Cartão, boleto e PIX",
        "image": "📲",
        "hint": "O endereço usa o domínio oficial da marca?",
        "signals": ["Domínio oficial", "Layout consistente", "Políticas visíveis"],
        "explanation": "A página usa domínio oficial e apresenta informações consistentes de compra."
    },
    {
        "id": 8,
        "store": "Netflx Renovação",
        "url": "https://netflx-renovar-conta.site",
        "type": "Golpe",
        "title": "Renovação de conta: seguro ou golpe?",
        "product": "Atualização de pagamento",
        "price": "Plano bloqueado",
        "payment": "Cartão de crédito",
        "image": "🎬",
        "hint": "Observe o nome do domínio e erros de marca.",
        "signals": ["Nome da marca escrito errado", "Domínio suspeito", "Captura de cartão"],
        "explanation": "O domínio usa uma grafia parecida com a marca, mas não é oficial. É uma tentativa típica de phishing."
    },
    {
        "id": 9,
        "store": "Americanas",
        "url": "https://www.americanas.com.br",
        "type": "Seguro",
        "title": "A promoção parece confiável?",
        "product": "Liquidificador 900W",
        "price": "R$ 189,90",
        "payment": "Cartão, boleto ou PIX",
        "image": "🍹",
        "hint": "Preço compatível e domínio oficial são bons sinais.",
        "signals": ["Domínio oficial", "Preço compatível", "Checkout convencional"],
        "explanation": "O cenário tem domínio oficial e condições de pagamento compatíveis com uma loja legítima."
    },
    {
        "id": 10,
        "store": "Leilão Eletrônicos Brasil",
        "url": "https://leilao-smartphones-brasil.click",
        "type": "Golpe",
        "title": "Leilão imperdível: seguro ou golpe?",
        "product": "Lote de smartphones",
        "price": "R$ 499,00",
        "payment": "PIX para reservar vaga",
        "image": "⚡",
        "hint": "Cuidado com promessa de ganho rápido e reserva por PIX.",
        "signals": ["Promessa exagerada", "Domínio estranho", "PIX antecipado"],
        "explanation": "O site usa promessa muito vantajosa, domínio pouco confiável e pagamento antecipado por PIX."
    }
]

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            percent REAL NOT NULL,
            used_hints INTEGER NOT NULL,
            answers_json TEXT NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)
    conn.commit()
    conn.close()

@app.before_request
def prepare():
    init_db()

@app.route("/")
def index():
    return render_template("index.html", questions=QUESTIONS, user=session.get("user_email"))

@app.route("/api/questions")
def api_questions():
    safe_questions = []
    for q in QUESTIONS:
        item = dict(q)
        item.pop("type", None)
        safe_questions.append(item)
    return jsonify(safe_questions)

@app.route("/api/check", methods=["POST"])
def api_check():
    data = request.get_json(force=True)
    qid = int(data.get("id"))
    answer = data.get("answer")
    question = next((q for q in QUESTIONS if q["id"] == qid), None)
    if not question:
        return jsonify({"error": "Questão não encontrada"}), 404

    correct = answer == question["type"]
    return jsonify({
        "correct": correct,
        "correctAnswer": question["type"],
        "signals": question["signals"],
        "explanation": question["explanation"]
    })

@app.route("/api/signup", methods=["POST"])
def signup():
    data = request.get_json(force=True)
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""
    if not email or not password or len(password) < 6:
        return jsonify({"error": "Informe e-mail e senha com pelo menos 6 caracteres."}), 400

    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO users (email, password_hash, created_at) VALUES (?, ?, ?)",
            (email, generate_password_hash(password), datetime.utcnow().isoformat())
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"error": "Este e-mail já está cadastrado."}), 400

    user = conn.execute("SELECT id, email FROM users WHERE email = ?", (email,)).fetchone()
    conn.close()
    session["user_id"] = user["id"]
    session["user_email"] = user["email"]
    return jsonify({"ok": True, "email": user["email"]})

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json(force=True)
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    conn.close()
    if not user or not check_password_hash(user["password_hash"], password):
        return jsonify({"error": "E-mail ou senha inválidos."}), 401

    session["user_id"] = user["id"]
    session["user_email"] = user["email"]
    return jsonify({"ok": True, "email": user["email"]})

@app.route("/api/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"ok": True})

@app.route("/api/attempts", methods=["GET", "POST"])
def attempts():
    if not session.get("user_id"):
        return jsonify({"error": "Login necessário para histórico em nuvem."}), 401

    conn = get_db()
    if request.method == "POST":
        data = request.get_json(force=True)
        score = int(data.get("score", 0))
        total = int(data.get("total", 0))
        percent = float(data.get("percent", 0))
        used_hints = int(data.get("usedHints", 0))
        answers = data.get("answers", [])
        conn.execute(
            """
            INSERT INTO attempts (user_id, score, total, percent, used_hints, answers_json, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (session["user_id"], score, total, percent, used_hints, json.dumps(answers, ensure_ascii=False), datetime.utcnow().isoformat())
        )
        conn.commit()
        conn.close()
        return jsonify({"ok": True})

    rows = conn.execute(
        "SELECT score, total, percent, used_hints, created_at FROM attempts WHERE user_id = ? ORDER BY id DESC LIMIT 20",
        (session["user_id"],)
    ).fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
