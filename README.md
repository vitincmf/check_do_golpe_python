
# Check do Golpe — Simulador Educativo em Python

Implementação em Python/Flask baseada nas Fases 1, 2 e 3 do projeto.

## Funcionalidades implementadas

- Quiz mobile-first.
- 10 questões com cenários seguros e fraudulentos.
- Botões "É um Golpe!" e "É Seguro!".
- Feedback imediato após cada resposta.
- Pontuação e progresso.
- Dicas opcionais.
- Resultado final com acertos, erros e percentual.
- Progresso local com localStorage.
- Cadastro/login opcionais.
- Histórico de tentativas para usuários autenticados.
- Banco SQLite.
- Estrutura PWA básica com manifest e service worker.

## Como executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute:

```bash
python app.py
```

3. Acesse no navegador:

```bash
http://127.0.0.1:5000
```

## Observação

Para ambiente de produção, troque a `secret_key` do Flask e use HTTPS.
