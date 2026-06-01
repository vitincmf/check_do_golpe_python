import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from database import get_connection, create_database, placeholder


def seed_database():

    create_database()

    conn = get_connection()
    cursor = conn.cursor()
    p = placeholder()

    print("Iniciando seed...")

    # =====================
    # FAIXAS ETÁRIAS
    # =====================

    faixas = [
        "Até 17 anos",
        "18 a 29 anos",
        "30 a 49 anos",
        "50 anos ou mais"
    ]

    for faixa in faixas:
        cursor.execute(
            f"""
            INSERT INTO faixas_etarias (nome)
            VALUES ({p})
            ON CONFLICT (nome) DO NOTHING
            """,
            (faixa,)
        )


    # =====================
    # GRUPOS
    # =====================

    grupos_perfil = [

        (
            "Grupo 1",
            "Pouca experiência",
            "Raramente compra online, usa pouco a internet, pode ter dificuldade com tecnologia.",
            "Principal público-alvo do golpe."
        ),

        (
            "Grupo 2",
            "Experiência moderada",
            "Compra online às vezes, usa redes sociais e aplicativos.",
            "Perfil intermediário."
        ),

        (
            "Grupo 3",
            "Experiência frequente",
            "Compra online regularmente e reconhece ameaças digitais.",
            "Usuário mais preparado digitalmente."
        )

    ]


    for grupo in grupos_perfil:
        cursor.execute(
            f"""
            INSERT INTO grupos_perfil
            (
                nome,
                perfil,
                caracteristicas,
                relevancia
            )
            VALUES ({p},{p},{p},{p})
            ON CONFLICT (nome) DO NOTHING
            """,
            grupo
        )


    # =====================
    # ASSUNTOS
    # =====================

    assuntos = [

        (
            "Golpes bancários",
            "Fraudes envolvendo bancos e dados financeiros."
        ),

        (
            "Sites falsos / E-commerce fake",
            "Lojas falsas e páginas clonadas."
        ),

        (
            "Correios e entregas",
            "Golpes de rastreamento e taxas falsas."
        ),

        (
            "Phishing por e-mail",
            "Mensagens falsas roubando informações."
        ),

        (
            "WhatsApp e redes sociais",
            "Perfis falsos e mensagens fraudulentas."
        ),

        (
            "Pix e pagamentos",
            "Golpes envolvendo pagamentos digitais."
        ),

        (
            "Falsos investimentos",
            "Promessas falsas de lucro rápido."
        ),

        (
            "Golpes com dados pessoais",
            "Roubo de CPF e informações privadas."
        ),

        (
            "IA, Deepfake e Engenharia Social",
            "Golpes modernos usando inteligência artificial."
        )

    ]


    for assunto in assuntos:
        cursor.execute(
            f"""
            INSERT INTO assuntos
            (
                nome,
                descricao
            )
            VALUES ({p},{p})
            ON CONFLICT (nome) DO NOTHING
            """,
            assunto
        )


    conn.commit()
    conn.close()

    print("SEED FINALIZADO COM SUCESSO!")


def inserir_dados():
    seed_database()


if __name__ == "__main__":
    seed_database()