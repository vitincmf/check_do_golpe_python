import os
import sqlite3


SQLITE_DATABASE = "check_do_golpe.db"


try:
    import psycopg2
    import psycopg2.extras
except ImportError:
    psycopg2 = None


def get_database_url():
    return os.getenv("DATABASE_URL", "").strip()
print("DATABASE_URL:", get_database_url()[:20])
print("POSTGRES ATIVO:", get_database_url().startswith("postgres"))


def is_postgres():
    return psycopg2 is not None and get_database_url().startswith("postgres")


def get_connection():

    if is_postgres():

        return psycopg2.connect(
            get_database_url(),
            cursor_factory=psycopg2.extras.RealDictCursor
        )

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
        return dict(row)

    return row


def fetchall(cursor):

    rows = cursor.fetchall()

    if is_postgres():
        return [dict(r) for r in rows]

    return rows


def create_database():

    conn = get_connection()
    cursor = conn.cursor()

    if is_postgres():

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS faixas_etarias (
                id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL UNIQUE
            )
        """)


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS grupos_perfil (
                id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL UNIQUE,
                perfil TEXT NOT NULL,
                caracteristicas TEXT NOT NULL,
                relevancia TEXT NOT NULL
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
                grupo_perfil_id INTEGER REFERENCES grupos_perfil(id),
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
                resposta_correta TEXT NOT NULL,
                explicacao TEXT NOT NULL,
                dica TEXT,
                pontos INTEGER DEFAULT 10,
                assunto_id INTEGER REFERENCES assuntos(id),
                ativo INTEGER DEFAULT 1
            )
        """)


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tentativas (
                id SERIAL PRIMARY KEY,
                usuario_id INTEGER REFERENCES usuarios(id),
                visitante_id TEXT,
                faixa_etaria_id INTEGER REFERENCES faixas_etarias(id),
                grupo_perfil_id INTEGER REFERENCES grupos_perfil(id),
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
                tentativa_id INTEGER REFERENCES tentativas(id),
                questao_id INTEGER REFERENCES questoes(id),
                resposta_usuario TEXT NOT NULL,
                acertou INTEGER NOT NULL,
                usou_dica INTEGER DEFAULT 0,
                pontos_obtidos INTEGER DEFAULT 0,
                respondida_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


        cursor.execute("""
            ALTER TABLE usuarios
            ADD COLUMN IF NOT EXISTS grupo_perfil_id INTEGER
        """)


        cursor.execute("""
            ALTER TABLE tentativas
            ADD COLUMN IF NOT EXISTS grupo_perfil_id INTEGER
        """)


    else:

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS faixas_etarias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT UNIQUE
            )
        """)


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS grupos_perfil (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT UNIQUE,
                perfil TEXT,
                caracteristicas TEXT,
                relevancia TEXT
            )
        """)


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS assuntos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT UNIQUE,
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
                grupo_perfil_id INTEGER,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS questoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                descricao TEXT,
                url_simulada TEXT,
                imagem TEXT,
                resposta_correta TEXT,
                explicacao TEXT,
                dica TEXT,
                pontos INTEGER DEFAULT 10,
                assunto_id INTEGER,
                ativo INTEGER DEFAULT 1
            )
        """)


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tentativas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER,
                visitante_id TEXT,
                faixa_etaria_id INTEGER,
                grupo_perfil_id INTEGER,
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
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tentativa_id INTEGER,
                questao_id INTEGER,
                resposta_usuario TEXT,
                acertou INTEGER,
                usou_dica INTEGER DEFAULT 0,
                pontos_obtidos INTEGER DEFAULT 0,
                respondida_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


    conn.commit()
    conn.close()