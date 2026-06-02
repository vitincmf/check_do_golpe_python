import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise Exception("DATABASE_URL não encontrada no .env")

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

print("POSTGRES ATIVO:", True)

assuntos = [
    ("Golpes bancários", "Fraudes envolvendo bancos, contas, cartões, senhas e falsos atendimentos."),
    ("Sites falsos / E-commerce fake", "Golpes envolvendo lojas virtuais falsas, ofertas irreais e compras online fraudulentas."),
    ("Correios e entregas", "Golpes envolvendo rastreamento falso, taxas indevidas e falsas mensagens de entrega."),
    ("Phishing por e-mail", "Mensagens falsas por e-mail usadas para roubar dados, senhas ou induzir cliques suspeitos."),
    ("WhatsApp e redes sociais", "Golpes aplicados por mensagens, perfis falsos, contatos clonados e redes sociais."),
    ("Pix e pagamentos", "Fraudes envolvendo Pix, QR Code, comprovantes falsos e pagamentos antecipados."),
    ("Falsos investimentos", "Promessas falsas de lucro rápido, retorno garantido e oportunidades financeiras fraudulentas."),
    ("Golpes com dados pessoais", "Golpes que tentam obter CPF, documentos, fotos, dados bancários e informações sensíveis."),
    ("IA, Deepfake e Engenharia Social", "Golpes modernos usando inteligência artificial, clonagem de voz, deepfake e manipulação social.")
]

for nome, descricao in assuntos:
    cursor.execute(
        """
        INSERT INTO assuntos (nome, descricao)
        VALUES (%s, %s)
        ON CONFLICT (nome)
        DO UPDATE SET descricao = EXCLUDED.descricao
        """,
        (nome, descricao)
    )

conn.commit()

cursor.execute("SELECT COUNT(*) FROM assuntos")
total = cursor.fetchone()[0]

print("---------------------")
print("SEED FINALIZADO")
print("ASSUNTOS NO BANCO:", total)
print("---------------------")

cursor.close()
conn.close()