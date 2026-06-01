import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from database import get_connection, create_database, placeholder


def seed_database():
    create_database()

    conn = get_connection()
    cursor = conn.cursor()
    p = placeholder()

    faixas = [
        "Até 17 anos",
        "18 a 29 anos",
        "30 a 49 anos",
        "50 anos ou mais"
    ]

    grupos_perfil = [
        (
            "Grupo 1",
            "Pouca experiência",
            "Raramente compra online, usa pouco a internet, pode ter dificuldade com tecnologia, faixa etária mais ampla.",
            "Principal público-alvo do golpe. O quiz precisa funcionar especialmente bem para este grupo."
        ),
        (
            "Grupo 2",
            "Experiência moderada",
            "Compra online às vezes, usa redes sociais e apps do dia a dia, mas não tem conhecimento técnico aprofundado.",
            "Perfil intermediário, frequente entre estudantes universitários."
        ),
        (
            "Grupo 3",
            "Experiência frequente",
            "Compra online com regularidade, familiarizado com segurança digital, identifica facilmente sites suspeitos.",
            "Serve como referência de desempenho esperado para quem já tem o letramento digital desenvolvido."
        )
    ]

    assuntos = [
        ("Golpes bancários", "Fraudes envolvendo bancos, login falso e dados financeiros."),
        ("Sites falsos / E-commerce fake", "Lojas falsas, promoções enganosas e páginas clonadas."),
        ("Correios e entregas", "Golpes envolvendo rastreio, taxas falsas e encomendas."),
        ("Phishing por e-mail", "Mensagens falsas tentando roubar dados do usuário."),
        ("WhatsApp e redes sociais", "Golpes aplicados por mensagens e perfis falsos."),
        ("Pix e pagamentos", "Fraudes envolvendo transferências, QR Codes e comprovantes."),
        ("Falsos investimentos", "Promessas falsas de lucro rápido."),
        ("Golpes com dados pessoais", "Tentativas de roubo de CPF, senhas e informações pessoais."),
        ("IA, Deepfake e Engenharia Social", "Golpes modernos envolvendo inteligência artificial, clonagem de voz, deepfakes e engenharia social."),
    ]

    for faixa in faixas:
        try:
            cursor.execute(f"INSERT INTO faixas_etarias (nome) VALUES ({p})", (faixa,))
            conn.commit()
        except Exception:
            conn.rollback()

    for grupo in grupos_perfil:
        try:
            cursor.execute(f"""
                INSERT INTO grupos_perfil (
                    nome,
                    perfil,
                    caracteristicas,
                    relevancia
                )
                VALUES ({p}, {p}, {p}, {p})
            """, grupo)
            conn.commit()
        except Exception:
            conn.rollback()

    for nome, descricao in assuntos:
        try:
            cursor.execute(f"INSERT INTO assuntos (nome, descricao) VALUES ({p}, {p})", (nome, descricao))
            conn.commit()
        except Exception:
            conn.rollback()

    conn.close()
    print("Banco criado e dados iniciais inseridos com sucesso!")


if __name__ == "__main__":
    seed_database()