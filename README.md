# Check do Golpe — Sistema Online Multiusuário

Sistema educativo em Flask para simulação de golpes digitais, com:
- Quiz mobile-first
- Cadastro opcional
- Login
- Banco online PostgreSQL
- Estatísticas centralizadas por faixa etária e assunto
- Compatibilidade local com SQLite
- PWA instalável

## Rodar localmente

```bash
pip install -r requirements.txt
python data/seed.py
python data/questoes_seed.py
python app.py
```

Acesse:

```text
http://127.0.0.1:5000
```

## Rodar online no Render

1. Suba o projeto no GitHub.
2. No Render, crie um PostgreSQL Database.
3. Crie um Web Service apontando para o repositório.
4. Build Command:

```bash
pip install -r requirements.txt
```

5. Start Command:

```bash
gunicorn app:app
```

6. Variáveis de ambiente:
   - `DATABASE_URL`: URL externa ou interna do PostgreSQL
   - `SECRET_KEY`: uma chave secreta qualquer

7. Depois de publicar, rode uma vez no Shell do Render:

```bash
python data/seed.py
python data/questoes_seed.py
```

## Observação

Com PostgreSQL online, todos os usuários acessam o mesmo sistema e as respostas ficam centralizadas no banco.
