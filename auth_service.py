from werkzeug.security import generate_password_hash, check_password_hash
from database import get_connection, is_postgres, placeholder, fetchone


def criar_usuario(nome, email, senha, faixa_etaria_id):
    conn = get_connection()
    cursor = conn.cursor()
    p = placeholder()

    senha_hash = generate_password_hash(senha)

    try:
        cursor.execute(
            f"""
            INSERT INTO usuarios (nome, email, senha, faixa_etaria_id)
            VALUES ({p}, {p}, {p}, {p})
            """,
            (nome, email, senha_hash, faixa_etaria_id)
        )
        conn.commit()
        return True, "Conta criada com sucesso."
    except Exception:
        conn.rollback()
        return False, "Não foi possível criar a conta. Talvez o e-mail já esteja cadastrado."
    finally:
        conn.close()


def autenticar_usuario(email, senha):
    conn = get_connection()
    cursor = conn.cursor()
    p = placeholder()

    cursor.execute(f"SELECT * FROM usuarios WHERE email = {p}", (email,))
    usuario = fetchone(cursor)
    conn.close()

    if not usuario:
        return None

    if not check_password_hash(usuario["senha"], senha):
        return None

    return usuario
