from database import get_connection, fetchone, fetchall, placeholder


def estatisticas_gerais():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            COUNT(r.id) AS total_respostas,
            COALESCE(SUM(r.acertou), 0) AS total_acertos,
            COUNT(r.id) - COALESCE(SUM(r.acertou), 0) AS total_erros,
            CASE 
                WHEN COUNT(r.id) = 0 THEN 0
                ELSE ROUND((COALESCE(SUM(r.acertou), 0) * 100.0) / COUNT(r.id), 2)
            END AS percentual_acerto
        FROM respostas r
    """)

    dados = fetchone(cursor)
    conn.close()
    return dados


def estatisticas_por_faixa_etaria():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            f.nome AS faixa_etaria,
            COUNT(r.id) AS total_respostas,
            COALESCE(SUM(r.acertou), 0) AS total_acertos,
            COUNT(r.id) - COALESCE(SUM(r.acertou), 0) AS total_erros,
            CASE 
                WHEN COUNT(r.id) = 0 THEN 0
                ELSE ROUND((COALESCE(SUM(r.acertou), 0) * 100.0) / COUNT(r.id), 2)
            END AS percentual_acerto
        FROM respostas r
        JOIN tentativas t ON r.tentativa_id = t.id
        JOIN faixas_etarias f ON t.faixa_etaria_id = f.id
        GROUP BY f.id, f.nome
        ORDER BY f.id
    """)

    dados = fetchall(cursor)
    conn.close()
    return dados


def estatisticas_por_assunto():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            a.nome AS assunto,
            COUNT(r.id) AS total_respostas,
            COALESCE(SUM(r.acertou), 0) AS total_acertos,
            COUNT(r.id) - COALESCE(SUM(r.acertou), 0) AS total_erros,
            CASE 
                WHEN COUNT(r.id) = 0 THEN 0
                ELSE ROUND((COALESCE(SUM(r.acertou), 0) * 100.0) / COUNT(r.id), 2)
            END AS percentual_acerto
        FROM respostas r
        JOIN questoes q ON r.questao_id = q.id
        JOIN assuntos a ON q.assunto_id = a.id
        GROUP BY a.id, a.nome
        ORDER BY percentual_acerto ASC
    """)

    dados = fetchall(cursor)
    conn.close()
    return dados


def estatisticas_por_idade_e_assunto():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            f.nome AS faixa_etaria,
            a.nome AS assunto,
            COUNT(r.id) AS total_respostas,
            COALESCE(SUM(r.acertou), 0) AS total_acertos,
            COUNT(r.id) - COALESCE(SUM(r.acertou), 0) AS total_erros,
            CASE 
                WHEN COUNT(r.id) = 0 THEN 0
                ELSE ROUND((COALESCE(SUM(r.acertou), 0) * 100.0) / COUNT(r.id), 2)
            END AS percentual_acerto
        FROM respostas r
        JOIN tentativas t ON r.tentativa_id = t.id
        JOIN faixas_etarias f ON t.faixa_etaria_id = f.id
        JOIN questoes q ON r.questao_id = q.id
        JOIN assuntos a ON q.assunto_id = a.id
        GROUP BY f.id, f.nome, a.id, a.nome
        ORDER BY f.id, percentual_acerto ASC
    """)

    dados = fetchall(cursor)
    conn.close()
    return dados


def questoes_mais_erradas(limite=10):
    conn = get_connection()
    cursor = conn.cursor()
    p = placeholder()

    cursor.execute(f"""
        SELECT
            q.titulo,
            a.nome AS assunto,
            COUNT(r.id) AS total_respostas,
            SUM(CASE WHEN r.acertou = 0 THEN 1 ELSE 0 END) AS total_erros,
            ROUND(
                (SUM(CASE WHEN r.acertou = 0 THEN 1 ELSE 0 END) * 100.0) / COUNT(r.id),
                2
            ) AS percentual_erro
        FROM respostas r
        JOIN questoes q ON r.questao_id = q.id
        JOIN assuntos a ON q.assunto_id = a.id
        GROUP BY q.id, q.titulo, a.nome
        HAVING COUNT(r.id) > 0
        ORDER BY percentual_erro DESC, total_erros DESC
        LIMIT {p}
    """, (limite,))

    dados = fetchall(cursor)
    conn.close()
    return dados
