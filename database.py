import os
import sqlite3

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
SQLITE_DATABASE = "check_do_golpe.db"

try:
    import psycopg2
    import psycopg2.extras
except ImportError:
    psycopg2 = None


def is_postgres():
    return (
        psycopg2 is not None
        and DATABASE_URL.startswith("postgres")
    )


def get_connection():
    if is_postgres():
        return psycopg2.connect(DATABASE_URL)

    conn = sqlite3.connect(SQLITE_DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def placeholder():
    return "%s" if is_postgres() else "?"


def fetchone(cursor):
    row = cursor.fetchone()

    if row is None:
        return None

    if is_postgres():
        if isinstance(row, dict):
            return row
        return dict(row)

    return row


def fetchall(cursor):
    rows = cursor.fetchall()

    if is_postgres():
        return [dict(r) for r in rows]

    return rows


def create_database():
    conn = get_connection()

    if is_postgres():
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    else:
        cursor = conn.cursor()

    if is_postgres():
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS faixas_etarias (
                id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS assuntos (
                id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL UNIQUE,
                descricao TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                nome TEXT,
                email TEXT UNIQUE,
                senha TEXT,
                faixa_etaria_id INTEGER REFERENCES faixas_etarias(id),
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS questoes (
                id SERIAL PRIMARY KEY,
                titulo TEXT NOT NULL,
                descricao TEXT NOT NULL,
                url_simulada TEXT,
                imagem TEXT,
                resposta_correta TEXT NOT NULL CHECK(resposta_correta IN ('seguro', 'golpe')),
                explicacao TEXT NOT NULL,
                dica TEXT,
                pontos INTEGER DEFAULT 10,
                assunto_id INTEGER NOT NULL REFERENCES assuntos(id),
                ativo INTEGER DEFAULT 1
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tentativas (
                id SERIAL PRIMARY KEY,
                usuario_id INTEGER REFERENCES usuarios(id),
                visitante_id TEXT,
                faixa_etaria_id INTEGER NOT NULL REFERENCES faixas_etarias(id),
                pontuacao_total INTEGER DEFAULT 0,
                total_questoes INTEGER DEFAULT 0,
                total_acertos INTEGER DEFAULT 0,
                total_erros INTEGER DEFAULT 0,
                finalizada INTEGER DEFAULT 0,
                criada_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS respostas (
                id SERIAL PRIMARY KEY,
                tentativa_id INTEGER NOT NULL REFERENCES tentativas(id),
                questao_id INTEGER NOT NULL REFERENCES questoes(id),
                resposta_usuario TEXT NOT NULL CHECK(resposta_usuario IN ('seguro', 'golpe')),
                acertou INTEGER NOT NULL,
                usou_dica INTEGER DEFAULT 0,
                pontos_obtidos INTEGER DEFAULT 0,
                respondida_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

    else:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS faixas_etarias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS assuntos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                descricao TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                email TEXT UNIQUE,
                senha TEXT,
                faixa_etaria_id INTEGER,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (faixa_etaria_id) REFERENCES faixas_etarias(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS questoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT NOT NULL,
                url_simulada TEXT,
                imagem TEXT,
                resposta_correta TEXT NOT NULL CHECK(resposta_correta IN ('seguro', 'golpe')),
                explicacao TEXT NOT NULL,
                dica TEXT,
                pontos INTEGER DEFAULT 10,
                assunto_id INTEGER NOT NULL,
                ativo INTEGER DEFAULT 1,
                FOREIGN KEY (assunto_id) REFERENCES assuntos(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tentativas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER,
                visitante_id TEXT,
                faixa_etaria_id INTEGER NOT NULL,
                pontuacao_total INTEGER DEFAULT 0,
                total_questoes INTEGER DEFAULT 0,
                total_acertos INTEGER DEFAULT 0,
                total_erros INTEGER DEFAULT 0,
                finalizada INTEGER DEFAULT 0,
                criada_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                FOREIGN KEY (faixa_etaria_id) REFERENCES faixas_etarias(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS respostas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tentativa_id INTEGER NOT NULL,
                questao_id INTEGER NOT NULL,
                resposta_usuario TEXT NOT NULL CHECK(resposta_usuario IN ('seguro', 'golpe')),
                acertou INTEGER NOT NULL,
                usou_dica INTEGER DEFAULT 0,
                pontos_obtidos INTEGER DEFAULT 0,
                respondida_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (tentativa_id) REFERENCES tentativas(id),
                FOREIGN KEY (questao_id) REFERENCES questoes(id)
            )
        """)

    conn.commit()
    conn.close()