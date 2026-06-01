import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from database import get_connection, create_database, placeholder, fetchone

print("USANDO DATABASE.PY:", ROOT_DIR / "database.py")

QUESTOES = [
    # GOLPES BANCÁRIOS
    {
        "assunto": "Golpes bancários",
        "titulo": "Área do cliente",
        "descricao": "Uma página informa que sua conta será bloqueada caso você não atualize seus dados.",
        "url_simulada": "http://banco-seguranca-cliente.com",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque usa urgência, domínio não oficial e tentativa de coletar dados bancários.",
        "dica": "Observe o domínio e a mensagem exibida.",
        "pontos": 10
    },
    {
        "assunto": "Golpes bancários",
        "titulo": "Mensagem recebida",
        "descricao": "Você recebe um SMS dizendo que uma compra de R$ 3.200 foi aprovada e apresenta um link para cancelamento.",
        "url_simulada": "http://cancelar-compra-banco.net",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque tenta assustar o usuário e levá-lo a acessar uma página não oficial.",
        "dica": "Bancos normalmente orientam o uso dos canais oficiais.",
        "pontos": 10
    },
    {
        "assunto": "Golpes bancários",
        "titulo": "Atendimento pelo aplicativo",
        "descricao": "Uma pessoa se apresenta como gerente do banco e pede confirmação de senha para resolver um problema na conta.",
        "url_simulada": "https://wa.me/gerente-seguranca",
        "resposta_correta": "golpe",
        "explicacao": "Gerentes e bancos não solicitam senhas por WhatsApp ou mensagens diretas.",
        "dica": "Nunca informe senha para terceiros.",
        "pontos": 10
    },
    {
        "assunto": "Golpes bancários",
        "titulo": "Aplicativo bancário",
        "descricao": "O usuário abre o aplicativo do banco instalado pela loja oficial do celular.",
        "url_simulada": "app://banco-oficial",
        "resposta_correta": "seguro",
        "explicacao": "É mais seguro acessar serviços bancários por aplicativo oficial obtido em loja confiável.",
        "dica": "Verifique se o app é oficial.",
        "pontos": 10
    },
    {
        "assunto": "Golpes bancários",
        "titulo": "Área de acesso",
        "descricao": "O usuário digita diretamente o endereço do banco no navegador e acessa com HTTPS.",
        "url_simulada": "https://www.bancooficial.com.br",
        "resposta_correta": "seguro",
        "explicacao": "O acesso parece seguro porque o endereço foi digitado diretamente e usa HTTPS.",
        "dica": "Prefira digitar o endereço oficial.",
        "pontos": 10
    },
    {
    "assunto": "Golpes bancários",
    "titulo": "Área do cliente",
    "descricao": "Uma página informa que foi identificada atividade incomum em sua conta e solicita confirmação de dados.",
    "url_simulada": "https://seguranca-cliente-banco.net",
    "resposta_correta": "golpe",
    "explicacao": "O domínio não pertence ao banco e solicita dados sensíveis.",
    "dica": "Observe cuidadosamente o endereço.",
    "pontos": 10
    },
    {
    "assunto": "Golpes bancários",
    "titulo": "Notificação recebida",
    "descricao": "Você recebe uma mensagem informando atualização obrigatória do cadastro bancário.",
    "url_simulada": "http://atualizacao-segura-conta.com",
    "resposta_correta": "golpe",
    "explicacao": "O endereço não corresponde ao domínio oficial da instituição.",
    "dica": "Compare o domínio com o oficial.",
    "pontos": 10
    } ,
    {
    "assunto": "Golpes bancários",
    "titulo": "Central de atendimento",
    "descricao": "Uma página solicita agência, conta, senha e token para validação de segurança.",
    "url_simulada": "https://validacao-cliente-online.org",
    "resposta_correta": "golpe",
    "explicacao": "Instituições financeiras não solicitam todos esses dados simultaneamente em páginas externas.",
    "dica": "Observe quais informações são exigidas.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Consulta de movimentação",
    "descricao": "O sistema informa uma transferência desconhecida e orienta acessar um link para bloqueio.",
    "url_simulada": "http://cancelamento-transacao.net",
    "resposta_correta": "golpe",
    "explicacao": "A estratégia usa medo para induzir acesso a página falsa.",
    "dica": "Analise a origem da página.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Atualização cadastral",
    "descricao": "Uma página informa necessidade de reenviar foto do cartão e documento.",
    "url_simulada": "https://cliente-verificacao.app",
    "resposta_correta": "golpe",
    "explicacao": "O domínio é estranho e solicita documentos sensíveis.",
    "dica": "Observe o endereço e os dados pedidos.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Acesso online",
    "descricao": "O usuário acessa sua conta utilizando o endereço oficial digitado manualmente.",
    "url_simulada": "https://www.bancooficial.com.br",
    "resposta_correta": "seguro",
    "explicacao": "O acesso foi realizado diretamente no domínio oficial.",
    "dica": "Verifique o domínio.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Aplicativo instalado",
    "descricao": "O usuário utiliza aplicativo obtido pela loja oficial do dispositivo.",
    "url_simulada": "app://banco-oficial",
    "resposta_correta": "seguro",
    "explicacao": "Aplicativos oficiais reduzem riscos de falsificação.",
    "dica": "Observe a origem do aplicativo.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Área de investimentos",
    "descricao": "Uma página apresenta informações financeiras sem solicitar senhas ou dados bancários.",
    "url_simulada": "https://www.bancooficial.com.br/investimentos",
    "resposta_correta": "seguro",
    "explicacao": "A navegação ocorre dentro do domínio legítimo.",
    "dica": "Confira o endereço completo.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Consulta de extrato",
    "descricao": "O usuário consulta movimentações através do aplicativo autenticado do banco.",
    "url_simulada": "app://extrato-banco",
    "resposta_correta": "seguro",
    "explicacao": "O acesso ocorre por canal legítimo da instituição.",
    "dica": "Observe o contexto da operação.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Portal financeiro",
    "descricao": "Uma página permite apenas consulta de informações públicas do banco.",
    "url_simulada": "https://www.bancooficial.com.br",
    "resposta_correta": "seguro",
    "explicacao": "Não há solicitação suspeita de credenciais ou dados sensíveis.",
    "dica": "Observe quais dados são solicitados.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Serviço ao cliente",
    "descricao": "Uma página informa necessidade de desbloqueio imediato da conta.",
    "url_simulada": "https://desbloqueio-banco-cliente.net",
    "resposta_correta": "golpe",
    "explicacao": "O domínio não pertence ao banco e utiliza senso de urgência.",
    "dica": "Analise o endereço.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Comunicado eletrônico",
    "descricao": "O sistema informa divergência cadastral e solicita atualização imediata.",
    "url_simulada": "http://dados-clientes-online.com",
    "resposta_correta": "golpe",
    "explicacao": "A página utiliza domínio genérico sem relação com a instituição.",
    "dica": "Verifique quem é o proprietário do domínio.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Painel de acesso",
    "descricao": "A página apresenta logotipo do banco e pede senha, token e código SMS simultaneamente.",
    "url_simulada": "https://seguranca-conta-banco.org",
    "resposta_correta": "golpe",
    "explicacao": "O conjunto de solicitações é incompatível com procedimentos normais.",
    "dica": "Observe os dados solicitados.",
    "pontos": 10
},
{
    "assunto": "Golpes bancários",
    "titulo": "Área do cliente",
    "descricao": "Uma página apresenta um formulário para consulta de saldo e utiliza o domínio oficial do banco.",
    "url_simulada": "https://www.bancooficial.com.br",
    "resposta_correta": "seguro",
    "explicacao": "O acesso ocorre em domínio legítimo da instituição financeira.",
    "dica": "Observe o endereço completo.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Portal de serviços",
    "descricao": "O usuário acessa uma área de atendimento disponível dentro do site oficial da instituição.",
    "url_simulada": "https://www.bancooficial.com.br/atendimento",
    "resposta_correta": "seguro",
    "explicacao": "A navegação ocorre em endereço legítimo e conhecido.",
    "dica": "Confira o domínio principal.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Consulta eletrônica",
    "descricao": "Uma página apresenta histórico de movimentações sem solicitar dados adicionais.",
    "url_simulada": "https://www.bancooficial.com.br/extrato",
    "resposta_correta": "seguro",
    "explicacao": "Não há solicitação suspeita e o domínio é legítimo.",
    "dica": "Observe o endereço e a finalidade da página.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Acesso à conta",
    "descricao": "O usuário acessa um ambiente bancário utilizando autenticação de dois fatores.",
    "url_simulada": "https://www.bancooficial.com.br/login",
    "resposta_correta": "seguro",
    "explicacao": "O uso de autenticação adicional aumenta a segurança.",
    "dica": "Observe o contexto do acesso.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Atualização de cadastro",
    "descricao": "Uma página informa necessidade de regularização imediata e solicita foto do cartão frente e verso.",
    "url_simulada": "https://cliente-validacao.net",
    "resposta_correta": "golpe",
    "explicacao": "Solicitação de imagens completas do cartão em domínio estranho é sinal de fraude.",
    "dica": "Observe os dados exigidos.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Comunicado recebido",
    "descricao": "Uma página informa que a conta será encerrada em poucas horas caso não seja realizada uma confirmação.",
    "url_simulada": "http://seguranca-bancaria-cliente.com",
    "resposta_correta": "golpe",
    "explicacao": "Urgência excessiva é característica comum em golpes digitais.",
    "dica": "Analise a mensagem e o domínio.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Serviço digital",
    "descricao": "Uma página pede número do cartão, senha e código SMS para liberar uma atualização.",
    "url_simulada": "https://cliente-online-seguro.org",
    "resposta_correta": "golpe",
    "explicacao": "A combinação dessas solicitações é incompatível com práticas legítimas.",
    "dica": "Observe quais informações são solicitadas.",
    "pontos": 10
},

{
    "assunto": "Golpes bancários",
    "titulo": "Área restrita",
    "descricao": "Uma página informa divergência de segurança e solicita validação completa dos dados bancários.",
    "url_simulada": "http://confirmacao-conta-bancaria.net",
    "resposta_correta": "golpe",
    "explicacao": "O domínio não pertence à instituição e busca coletar informações sensíveis.",
    "dica": "Confira o endereço da página.",
    "pontos": 10
},



    # E-COMMERCE
    {
        "assunto": "Sites falsos / E-commerce fake",
        "titulo": "Oferta encontrada",
        "descricao": "Uma loja virtual oferece um celular por R$ 899 e aceita pagamento via Pix.",
        "url_simulada": "https://megaoferta-celular.shop",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque o preço é incompatível com o mercado, o domínio não é conhecido e há forte indução ao pagamento por Pix.",
        "dica": "Compare preço, domínio e dados da loja.",
        "pontos": 10
    },
    {
        "assunto": "Sites falsos / E-commerce fake",
        "titulo": "Loja virtual",
        "descricao": "A loja vende produtos eletrônicos e apresenta uma página simples de compra.",
        "url_simulada": "https://superdesconto-total.site",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque a loja não apresenta identificação clara, CNPJ, endereço, telefone ou política de troca.",
        "dica": "Procure dados da loja antes de comprar.",
        "pontos": 10
    },
    {
        "assunto": "Sites falsos / E-commerce fake",
        "titulo": "Página de venda",
        "descricao": "Um site apresenta videogames com preço promocional e disponibilidade imediata.",
        "url_simulada": "https://games-promocao-relampago.shop",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque combina domínio pouco confiável, oferta muito vantajosa e pressão para compra.",
        "dica": "Compare preços em lojas confiáveis.",
        "pontos": 10
    },
    {
        "assunto": "Sites falsos / E-commerce fake",
        "titulo": "Loja virtual",
        "descricao": "Uma loja apresenta CNPJ, avaliações, política de troca e pagamento por cartão.",
        "url_simulada": "https://www.lojaconhecida.com.br",
        "resposta_correta": "seguro",
        "explicacao": "A loja apresenta sinais de confiabilidade e informações verificáveis.",
        "dica": "Verifique reputação e dados da empresa.",
        "pontos": 10
    },
    {
        "assunto": "Sites falsos / E-commerce fake",
        "titulo": "Compra online",
        "descricao": "O usuário compra por uma plataforma com proteção ao comprador e avaliações do vendedor.",
        "url_simulada": "https://www.marketplaceconfiavel.com.br",
        "resposta_correta": "seguro",
        "explicacao": "Marketplaces confiáveis oferecem mecanismos de proteção e reputação.",
        "dica": "Veja avaliações e garantias da plataforma.",
        "pontos": 10
    },
    {
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Página de compra",
    "descricao": "Uma loja apresenta diversos produtos eletrônicos e informa que o pagamento deve ser realizado exclusivamente por transferência antecipada.",
    "url_simulada": "https://compras-promocionais.shop",
    "resposta_correta": "golpe",
    "explicacao": "A exigência de pagamento antecipado sem outras garantias aumenta o risco de fraude.",
    "dica": "Observe as formas de pagamento disponíveis.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Catálogo virtual",
    "descricao": "Uma loja informa possuir estoque ilimitado para todos os produtos anunciados.",
    "url_simulada": "https://estoque-total.shop",
    "resposta_correta": "golpe",
    "explicacao": "Promessas pouco realistas podem indicar tentativa de atrair compradores sem compromisso com a entrega.",
    "dica": "Analise se as informações parecem plausíveis.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Página comercial",
    "descricao": "Uma loja apresenta preços muito inferiores aos encontrados em outras empresas do setor.",
    "url_simulada": "https://oferta-imperdivel-eletronicos.site",
    "resposta_correta": "golpe",
    "explicacao": "Diferenças exageradas de preço costumam ser utilizadas para atrair vítimas.",
    "dica": "Compare preços em diferentes lojas.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Loja online",
    "descricao": "O site informa endereço físico, telefone, CNPJ e canais de atendimento verificáveis.",
    "url_simulada": "https://www.lojaexemplo.com.br",
    "resposta_correta": "seguro",
    "explicacao": "Informações verificáveis aumentam a confiabilidade da empresa.",
    "dica": "Procure dados institucionais.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Página de compra",
    "descricao": "A plataforma disponibiliza política de troca, devolução e garantia claramente descritas.",
    "url_simulada": "https://www.comprasconfiaveis.com.br",
    "resposta_correta": "seguro",
    "explicacao": "Lojas legítimas costumam apresentar políticas transparentes.",
    "dica": "Leia as condições da compra.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Loja virtual",
    "descricao": "O usuário encontra avaliações da empresa em diferentes plataformas independentes.",
    "url_simulada": "https://www.lojareputacao.com.br",
    "resposta_correta": "seguro",
    "explicacao": "Avaliações externas ajudam a validar a reputação da loja.",
    "dica": "Pesquise fora do próprio site.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Marketplace",
    "descricao": "O vendedor possui histórico de vendas, comentários públicos e classificação visível.",
    "url_simulada": "https://www.marketplaceoficial.com.br",
    "resposta_correta": "seguro",
    "explicacao": "Informações públicas de reputação ajudam na tomada de decisão.",
    "dica": "Analise o histórico do vendedor.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Página institucional",
    "descricao": "A empresa disponibiliza atendimento por telefone, e-mail e chat em seu portal oficial.",
    "url_simulada": "https://www.lojasegura.com.br",
    "resposta_correta": "seguro",
    "explicacao": "A presença de canais oficiais aumenta a credibilidade.",
    "dica": "Verifique os meios de contato.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Catálogo de produtos",
    "descricao": "A plataforma informa prazo de entrega, custo de frete e rastreamento dos pedidos.",
    "url_simulada": "https://www.compraonline.com.br",
    "resposta_correta": "seguro",
    "explicacao": "Informações claras sobre a entrega são comuns em lojas legítimas.",
    "dica": "Observe a transparência das informações.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Portal comercial",
    "descricao": "O site utiliza HTTPS, apresenta identificação da empresa e disponibiliza suporte ao consumidor.",
    "url_simulada": "https://www.lojaverificada.com.br",
    "resposta_correta": "seguro",
    "explicacao": "A combinação desses elementos reduz indícios de fraude.",
    "dica": "Observe os sinais de legitimidade.",
    "pontos": 10
},
{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Página comercial",
    "descricao": "Uma loja informa que todos os produtos possuem frete gratuito para qualquer região do país.",
    "url_simulada": "https://frete-total-brasil.shop",
    "resposta_correta": "golpe",
    "explicacao": "Promessas muito vantajosas sem detalhes verificáveis podem indicar fraude.",
    "dica": "Analise se a oferta parece realista.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Portal de compras",
    "descricao": "Uma página informa que os preços promocionais terminam em poucos minutos.",
    "url_simulada": "https://comprar-agora-oferta.site",
    "resposta_correta": "golpe",
    "explicacao": "A criação de urgência artificial é comum em golpes virtuais.",
    "dica": "Observe tentativas de pressão para compra.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Loja virtual",
    "descricao": "Um site vende diversos eletrônicos e não apresenta informações de contato da empresa.",
    "url_simulada": "https://super-eletronicos-desconto.shop",
    "resposta_correta": "golpe",
    "explicacao": "A ausência de dados verificáveis reduz a confiabilidade da loja.",
    "dica": "Procure informações da empresa.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Página de venda",
    "descricao": "Uma loja oferece produtos importados por valores muito inferiores aos praticados no mercado.",
    "url_simulada": "https://importados-oficiais.site",
    "resposta_correta": "golpe",
    "explicacao": "Diferenças exageradas de preço são utilizadas para atrair vítimas.",
    "dica": "Compare os preços em outras lojas.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Catálogo virtual",
    "descricao": "A plataforma informa que todos os produtos possuem disponibilidade imediata e quantidade ilimitada.",
    "url_simulada": "https://estoque-infinito.shop",
    "resposta_correta": "golpe",
    "explicacao": "Informações pouco realistas podem indicar tentativa de enganar consumidores.",
    "dica": "Analise a coerência das informações.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Página comercial",
    "descricao": "Uma loja recém-criada apresenta apenas pagamento antecipado e nenhuma informação institucional.",
    "url_simulada": "https://mega-promocoes-online.site",
    "resposta_correta": "golpe",
    "explicacao": "Pouca transparência e pagamento antecipado aumentam o risco.",
    "dica": "Observe os dados disponíveis sobre a empresa.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Portal comercial",
    "descricao": "O site apresenta CNPJ, endereço físico e canais de atendimento verificáveis.",
    "url_simulada": "https://www.lojaempresa.com.br",
    "resposta_correta": "seguro",
    "explicacao": "Informações verificáveis aumentam a confiabilidade.",
    "dica": "Procure dados institucionais.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Loja online",
    "descricao": "O usuário encontra histórico de avaliações da empresa em plataformas independentes.",
    "url_simulada": "https://www.lojaavaliada.com.br",
    "resposta_correta": "seguro",
    "explicacao": "Avaliações externas ajudam a validar a reputação da empresa.",
    "dica": "Pesquise opiniões fora do site.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Página de compra",
    "descricao": "A empresa disponibiliza políticas de troca, garantia e devolução de forma transparente.",
    "url_simulada": "https://www.compragarantida.com.br",
    "resposta_correta": "seguro",
    "explicacao": "Transparência é característica comum de operações legítimas.",
    "dica": "Verifique as políticas da loja.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Marketplace",
    "descricao": "O vendedor possui histórico de vendas, reputação pública e avaliações verificáveis.",
    "url_simulada": "https://www.marketplaceconfiavel.com.br",
    "resposta_correta": "seguro",
    "explicacao": "Informações públicas ajudam a avaliar a confiabilidade.",
    "dica": "Observe a reputação do vendedor.",
    "pontos": 10
},

{
    "assunto": "Sites falsos / E-commerce fake",
    "titulo": "Loja virtual",
    "descricao": "O portal utiliza HTTPS, possui suporte ao cliente e informações consistentes sobre a empresa.",
    "url_simulada": "https://www.lojaconsolidada.com.br",
    "resposta_correta": "seguro",
    "explicacao": "A combinação desses elementos reduz indícios de fraude.",
    "dica": "Analise o conjunto de informações disponíveis.",
    "pontos": 10
},

    # CORREIOS
    {
        "assunto": "Correios e entregas",
        "titulo": "Aviso de entrega",
        "descricao": "Mensagem informa que sua encomenda está retida e apresenta uma página para pagamento de uma taxa.",
        "url_simulada": "https://correios-taxas-entrega.net",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque o domínio não é oficial dos Correios e a página induz pagamento em ambiente externo.",
        "dica": "Compare o domínio com o site oficial.",
        "pontos": 10
    },
    {
        "assunto": "Correios e entregas",
        "titulo": "Aviso de entrega",
        "descricao": "Você recebe uma mensagem dizendo que sua entrega foi cancelada e apresenta uma página para reagendamento.",
        "url_simulada": "https://reagendar-entrega-correios.site",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque o endereço simula os Correios, mas não pertence ao domínio oficial.",
        "dica": "Confira o domínio antes de inserir dados ou pagar taxas.",
        "pontos": 10
    },
    {
        "assunto": "Correios e entregas",
        "titulo": "Atualização de entrega",
        "descricao": "Uma mensagem informa que uma encomenda internacional foi retida e apresenta uma página para pagamento.",
        "url_simulada": "https://taxa-alfandega-entrega.net",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque usa cobrança de entrega como isca e direciona para domínio não oficial.",
        "dica": "Confira o código no site oficial.",
        "pontos": 10
    },
    {
        "assunto": "Correios e entregas",
        "titulo": "Consulta de entrega",
        "descricao": "O usuário acessa diretamente o site dos Correios para consultar o rastreamento.",
        "url_simulada": "https://www.correios.com.br",
        "resposta_correta": "seguro",
        "explicacao": "A consulta é segura porque ocorre no domínio oficial.",
        "dica": "Prefira acessar o site oficial diretamente.",
        "pontos": 10
    },
    {
        "assunto": "Correios e entregas",
        "titulo": "Aplicativo de rastreamento",
        "descricao": "O usuário usa aplicativo instalado pela loja do celular para acompanhar uma entrega.",
        "url_simulada": "app://correios-oficial",
        "resposta_correta": "seguro",
        "explicacao": "Aplicativos oficiais reduzem o risco de acessar páginas não oficiais.",
        "dica": "Confira o desenvolvedor do aplicativo.",
        "pontos": 10
    },
    {
    "assunto": "Correios e entregas",
    "titulo": "Consulta de rastreamento",
    "descricao": "Uma página informa que existe uma atualização sobre sua encomenda e disponibiliza um código para consulta.",
    "url_simulada": "https://rastreamento-correios-online.net",
    "resposta_correta": "golpe",
    "explicacao": "O endereço não pertence ao domínio oficial dos Correios.",
    "dica": "Observe cuidadosamente o domínio.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Atualização de entrega",
    "descricao": "Uma página informa que existe uma pendência relacionada ao transporte da encomenda.",
    "url_simulada": "https://correios-entrega-pendente.site",
    "resposta_correta": "golpe",
    "explicacao": "O endereço tenta simular um serviço oficial dos Correios.",
    "dica": "Compare o domínio com o endereço oficial.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Informação de encomenda",
    "descricao": "Uma mensagem informa que existe uma atualização importante sobre uma entrega internacional.",
    "url_simulada": "https://liberacao-encomendas-br.net",
    "resposta_correta": "golpe",
    "explicacao": "O domínio não possui vínculo oficial com os Correios.",
    "dica": "Analise o endereço exibido.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Aviso de retirada",
    "descricao": "Uma página informa que uma encomenda aguarda retirada em uma unidade de atendimento.",
    "url_simulada": "https://agencia-retirada-correios.site",
    "resposta_correta": "golpe",
    "explicacao": "O endereço não corresponde ao portal oficial dos Correios.",
    "dica": "Verifique o domínio completo.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Acompanhamento logístico",
    "descricao": "Uma página informa que ocorreu uma alteração na rota de transporte da encomenda.",
    "url_simulada": "https://logistica-entrega-brasil.net",
    "resposta_correta": "golpe",
    "explicacao": "O domínio não pertence aos Correios e tenta parecer oficial.",
    "dica": "Observe quem é o responsável pela página.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Consulta de entrega",
    "descricao": "O usuário acessa diretamente o portal oficial para consultar um código de rastreamento.",
    "url_simulada": "https://www.correios.com.br",
    "resposta_correta": "seguro",
    "explicacao": "A consulta ocorre diretamente no domínio oficial dos Correios.",
    "dica": "Prefira acessar o endereço oficial manualmente.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Aplicativo de rastreamento",
    "descricao": "O usuário acompanha suas entregas utilizando um aplicativo oficial instalado pela loja do celular.",
    "url_simulada": "app://correios-oficial",
    "resposta_correta": "seguro",
    "explicacao": "Aplicativos oficiais reduzem o risco de páginas falsas.",
    "dica": "Confira quem desenvolveu o aplicativo.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Portal de atendimento",
    "descricao": "Uma página apresenta informações institucionais, rastreamento e canais oficiais de atendimento.",
    "url_simulada": "https://www.correios.com.br",
    "resposta_correta": "seguro",
    "explicacao": "O endereço corresponde ao portal oficial dos Correios.",
    "dica": "Observe o domínio principal.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Serviço de rastreio",
    "descricao": "O usuário consulta a situação de uma encomenda acessando diretamente o endereço oficial.",
    "url_simulada": "https://www.correios.com.br",
    "resposta_correta": "seguro",
    "explicacao": "O acesso foi realizado diretamente no portal oficial.",
    "dica": "Evite links recebidos por mensagens.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Consulta logística",
    "descricao": "Uma plataforma apresenta histórico completo da movimentação de uma encomenda.",
    "url_simulada": "https://www.correios.com.br",
    "resposta_correta": "seguro",
    "explicacao": "O serviço é disponibilizado pelo domínio oficial dos Correios.",
    "dica": "Confira sempre o endereço do site.",
    "pontos": 10
},
{
    "assunto": "Correios e entregas",
    "titulo": "Informação de entrega",
    "descricao": "Uma página informa que existe uma atualização importante relacionada a uma encomenda em trânsito.",
    "url_simulada": "https://rastreio-entrega-br.net",
    "resposta_correta": "golpe",
    "explicacao": "O endereço não pertence ao domínio oficial dos Correios.",
    "dica": "Observe cuidadosamente o domínio.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Notificação recebida",
    "descricao": "Uma mensagem informa que há uma pendência relacionada ao endereço de entrega.",
    "url_simulada": "https://confirmacao-entrega-correios.site",
    "resposta_correta": "golpe",
    "explicacao": "O domínio tenta se passar por serviço oficial.",
    "dica": "Compare com o domínio oficial.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Atualização logística",
    "descricao": "Uma página informa que a encomenda retornará ao remetente caso nenhuma ação seja tomada.",
    "url_simulada": "https://entrega-retorno-brasil.net",
    "resposta_correta": "golpe",
    "explicacao": "O domínio não possui relação oficial com os Correios.",
    "dica": "Observe quem é o proprietário do site.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Consulta de encomenda",
    "descricao": "Uma página apresenta detalhes de rastreamento e solicita confirmação de dados pessoais.",
    "url_simulada": "https://rastreamento-cliente-correios.site",
    "resposta_correta": "golpe",
    "explicacao": "A página associa rastreamento à coleta de dados pessoais.",
    "dica": "Observe as informações solicitadas.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Portal de rastreio",
    "descricao": "Uma página apresenta informações de entrega e direciona para uma área de pagamento.",
    "url_simulada": "https://liberacao-rastreamento.net",
    "resposta_correta": "golpe",
    "explicacao": "O domínio não é oficial e busca direcionar o usuário para procedimentos indevidos.",
    "dica": "Analise o endereço exibido.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Consulta de objeto",
    "descricao": "O usuário acompanha uma encomenda acessando diretamente o portal oficial.",
    "url_simulada": "https://www.correios.com.br",
    "resposta_correta": "seguro",
    "explicacao": "A consulta ocorre em ambiente oficial.",
    "dica": "Observe o domínio principal.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Acompanhamento de entrega",
    "descricao": "O usuário utiliza o sistema oficial para verificar a movimentação de uma encomenda.",
    "url_simulada": "https://www.correios.com.br",
    "resposta_correta": "seguro",
    "explicacao": "O serviço é fornecido diretamente pelos Correios.",
    "dica": "Verifique o endereço acessado.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Portal institucional",
    "descricao": "Uma página apresenta informações institucionais e canais de atendimento da empresa.",
    "url_simulada": "https://www.correios.com.br",
    "resposta_correta": "seguro",
    "explicacao": "O domínio pertence aos Correios.",
    "dica": "Observe o endereço principal.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Sistema de rastreamento",
    "descricao": "O usuário consulta o histórico completo de movimentações da encomenda.",
    "url_simulada": "https://www.correios.com.br",
    "resposta_correta": "seguro",
    "explicacao": "A funcionalidade é oferecida pelo portal oficial.",
    "dica": "Confira o domínio.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Aplicativo móvel",
    "descricao": "O acompanhamento da entrega é realizado através de aplicativo oficial.",
    "url_simulada": "app://correios-oficial",
    "resposta_correta": "seguro",
    "explicacao": "Aplicativos oficiais reduzem riscos de falsificação.",
    "dica": "Verifique a origem do aplicativo.",
    "pontos": 10
},

{
    "assunto": "Correios e entregas",
    "titulo": "Consulta de rastreio",
    "descricao": "O usuário acessa diretamente um portal conhecido para verificar a situação de sua encomenda.",
    "url_simulada": "https://www.correios.com.br",
    "resposta_correta": "seguro",
    "explicacao": "O acesso foi realizado diretamente no serviço oficial.",
    "dica": "Prefira digitar o endereço manualmente.",
    "pontos": 10
},

    # PHISHING
    {
        "assunto": "Phishing por e-mail",
        "titulo": "Mensagem recebida",
        "descricao": "Um e-mail informa que sua conta será encerrada e apresenta um formulário para preenchimento.",
        "url_simulada": "http://suporte-conta-verificacao.net",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque serviços legítimos não solicitam senha por formulário enviado por e-mail.",
        "dica": "Observe o domínio e os dados solicitados.",
        "pontos": 10
    },
    {
        "assunto": "Phishing por e-mail",
        "titulo": "Nota fiscal recebida",
        "descricao": "Você recebe um e-mail com uma suposta nota fiscal de compra que não realizou.",
        "url_simulada": "http://nota-fiscal-cliente-download.net",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque anexos ou links inesperados podem ser usados para roubar dados ou instalar programas maliciosos.",
        "dica": "Desconfie de cobranças que você não reconhece.",
        "pontos": 10
    },
    {
        "assunto": "Phishing por e-mail",
        "titulo": "Notificação de serviço",
        "descricao": "A mensagem parece ser de uma empresa conhecida e apresenta um link para atendimento.",
        "url_simulada": "http://atendimento-empresaoficia1.com",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque o domínio tenta imitar uma empresa conhecida usando escrita parecida.",
        "dica": "Observe pequenos erros no endereço.",
        "pontos": 10
    },
    {
        "assunto": "Phishing por e-mail",
        "titulo": "Notificação de serviço",
        "descricao": "Um serviço envia uma notificação sem pedir senha, pagamento ou informações pessoais.",
        "url_simulada": "https://www.servicooficial.com",
        "resposta_correta": "seguro",
        "explicacao": "A mensagem não solicita dados sensíveis nem direciona para página não oficial.",
        "dica": "Veja se há pedido de dados.",
        "pontos": 10
    },
    {
    "assunto": "Phishing por e-mail",
    "titulo": "Atualização de cadastro",
    "descricao": "Um e-mail informa que algumas informações da sua conta precisam ser atualizadas para evitar restrições futuras.",
    "url_simulada": "http://validacao-cliente-seguro.net",
    "resposta_correta": "golpe",
    "explicacao": "O domínio não pertence ao serviço legítimo e tenta induzir o usuário a fornecer informações.",
    "dica": "Observe cuidadosamente o endereço.",
    "pontos": 10
},

{
    "assunto": "Phishing por e-mail",
    "titulo": "Comunicado recebido",
    "descricao": "Uma mensagem informa que existe uma pendência em sua conta e apresenta um botão para regularização.",
    "url_simulada": "http://regularizacao-online-cliente.site",
    "resposta_correta": "golpe",
    "explicacao": "O domínio tenta parecer oficial para coletar dados.",
    "dica": "Confira se o endereço pertence à empresa.",
    "pontos": 10
},

{
    "assunto": "Phishing por e-mail",
    "titulo": "Verificação de acesso",
    "descricao": "Uma mensagem informa que foi detectado um acesso incomum e apresenta um link para validação.",
    "url_simulada": "http://seguranca-acesso-cliente.net",
    "resposta_correta": "golpe",
    "explicacao": "Criminosos usam alertas de segurança para induzir cliques.",
    "dica": "Analise o domínio antes de prosseguir.",
    "pontos": 10
},

{
    "assunto": "Phishing por e-mail",
    "titulo": "Documento disponível",
    "descricao": "Um e-mail informa que existe um documento aguardando assinatura eletrônica.",
    "url_simulada": "http://assinatura-documento-online.site",
    "resposta_correta": "golpe",
    "explicacao": "O endereço não corresponde a um serviço legítimo conhecido.",
    "dica": "Verifique a origem da solicitação.",
    "pontos": 10
},

{
    "assunto": "Phishing por e-mail",
    "titulo": "Aviso importante",
    "descricao": "Uma mensagem informa que sua conta será suspensa caso nenhuma ação seja realizada.",
    "url_simulada": "http://conta-segura-validacao.net",
    "resposta_correta": "golpe",
    "explicacao": "A urgência é usada para pressionar decisões rápidas.",
    "dica": "Desconfie de ameaças imediatas.",
    "pontos": 10
},

{
    "assunto": "Phishing por e-mail",
    "titulo": "Notificação recebida",
    "descricao": "Um e-mail apresenta um link para visualizar informações confidenciais da conta.",
    "url_simulada": "http://painel-cliente-acesso.site",
    "resposta_correta": "golpe",
    "explicacao": "O domínio não possui relação com o serviço mencionado.",
    "dica": "Observe o endereço completo.",
    "pontos": 10
},

{
    "assunto": "Phishing por e-mail",
    "titulo": "Mensagem automática",
    "descricao": "Uma mensagem informa que existe uma atualização obrigatória relacionada à sua conta.",
    "url_simulada": "http://atualizacao-sistema-cliente.net",
    "resposta_correta": "golpe",
    "explicacao": "Atualizações legítimas normalmente ocorrem dentro do serviço oficial.",
    "dica": "Analise o domínio apresentado.",
    "pontos": 10
},
{
    "assunto": "Phishing por e-mail",
    "titulo": "Notificação de serviço",
    "descricao": "Um serviço envia uma mensagem informativa sem solicitar senha, pagamento ou dados pessoais.",
    "url_simulada": "https://www.servicooficial.com",
    "resposta_correta": "seguro",
    "explicacao": "A comunicação não solicita informações sensíveis.",
    "dica": "Observe o conteúdo da mensagem.",
    "pontos": 10
},

{
    "assunto": "Phishing por e-mail",
    "titulo": "Aviso institucional",
    "descricao": "Uma empresa envia comunicado informando alterações em seus termos de uso.",
    "url_simulada": "https://www.empresaoficial.com.br",
    "resposta_correta": "seguro",
    "explicacao": "A comunicação parte do domínio oficial da empresa.",
    "dica": "Confira o domínio do remetente.",
    "pontos": 10
},

{
    "assunto": "Phishing por e-mail",
    "titulo": "Confirmação de cadastro",
    "descricao": "O usuário recebe um e-mail referente a uma conta criada recentemente por ele.",
    "url_simulada": "https://www.servicooficial.com",
    "resposta_correta": "seguro",
    "explicacao": "O contexto é compatível com uma ação realizada pelo usuário.",
    "dica": "Considere o contexto da mensagem.",
    "pontos": 10
},

{
    "assunto": "Phishing por e-mail",
    "titulo": "Mensagem informativa",
    "descricao": "Uma empresa envia um boletim com novidades e não solicita qualquer dado pessoal.",
    "url_simulada": "https://www.empresaoficial.com.br",
    "resposta_correta": "seguro",
    "explicacao": "Não há solicitação de informações sensíveis.",
    "dica": "Observe se existe pedido de dados.",
    "pontos": 10
},

{
    "assunto": "Phishing por e-mail",
    "titulo": "Atualização de serviço",
    "descricao": "Uma plataforma comunica melhorias em seus recursos através de seu domínio oficial.",
    "url_simulada": "https://www.plataformaoficial.com.br",
    "resposta_correta": "seguro",
    "explicacao": "A comunicação utiliza o domínio legítimo do serviço.",
    "dica": "Verifique a origem da mensagem.",
    "pontos": 10
},

{
    "assunto": "Phishing por e-mail",
    "titulo": "Comunicado institucional",
    "descricao": "Uma organização envia um aviso geral para seus usuários cadastrados.",
    "url_simulada": "https://www.organizacaooficial.org",
    "resposta_correta": "seguro",
    "explicacao": "A mensagem não solicita ações suspeitas.",
    "dica": "Observe o conteúdo e o domínio.",
    "pontos": 10
},

{
    "assunto": "Phishing por e-mail",
    "titulo": "Informação de suporte",
    "descricao": "O usuário recebe uma resposta referente a um chamado aberto anteriormente.",
    "url_simulada": "https://www.suporteoficial.com.br",
    "resposta_correta": "seguro",
    "explicacao": "A comunicação está relacionada a uma solicitação legítima.",
    "dica": "Considere o contexto do contato.",
    "pontos": 10
},

{
    "assunto": "Phishing por e-mail",
    "titulo": "Aviso de manutenção",
    "descricao": "Uma empresa informa previamente uma manutenção programada em seus sistemas.",
    "url_simulada": "https://www.empresaoficial.com.br",
    "resposta_correta": "seguro",
    "explicacao": "O aviso utiliza canais legítimos da empresa.",
    "dica": "Observe a procedência da mensagem.",
    "pontos": 10
},

{
    "assunto": "Phishing por e-mail",
    "titulo": "Comunicado ao usuário",
    "descricao": "Uma plataforma envia orientações gerais sobre segurança digital.",
    "url_simulada": "https://www.plataformaoficial.com.br",
    "resposta_correta": "seguro",
    "explicacao": "A mensagem possui caráter educativo e não solicita dados.",
    "dica": "Verifique se existe pedido de informações.",
    "pontos": 10
},

    # WHATSAPP
    {
        "assunto": "WhatsApp e redes sociais",
        "titulo": "Mensagem de contato",
        "descricao": "Uma pessoa diz ser seu familiar, afirma que trocou de número e pede uma transferência.",
        "url_simulada": "https://wa.me/numero-novo-familiar",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque criminosos se passam por familiares para pedir dinheiro.",
        "dica": "Confirme por ligação antes de transferir.",
        "pontos": 10
    },
    {
        "assunto": "WhatsApp e redes sociais",
        "titulo": "Promoção especial",
        "descricao": "Mensagem informa que você foi selecionado para receber um prêmio e apresenta um link para cadastro.",
        "url_simulada": "https://premio-especial-whatsapp.site",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque usa promessa de prêmio e link externo para capturar dados.",
        "dica": "Desconfie de prêmios que você não solicitou.",
        "pontos": 10
    },
    {
        "assunto": "WhatsApp e redes sociais",
        "titulo": "Confirmação de acesso",
        "descricao": "Um contato pede que você envie um código recebido por SMS para confirmar uma promoção.",
        "url_simulada": "https://confirmar-promocao-codigo.site",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque esse código pode permitir acesso indevido à sua conta.",
        "dica": "Nunca compartilhe códigos de verificação.",
        "pontos": 10
    },
    {
        "assunto": "WhatsApp e redes sociais",
        "titulo": "Publicação em rede social",
        "descricao": "Uma instituição publica em perfil verificado uma orientação de segurança, sem pedir dados pessoais.",
        "url_simulada": "https://www.instagram.com/instituicaooficial",
        "resposta_correta": "seguro",
        "explicacao": "A publicação vem de canal oficial e não solicita dados sensíveis.",
        "dica": "Verifique se o perfil é oficial.",
        "pontos": 10
    },
    {
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Mensagem recebida",
    "descricao": "Uma pessoa informa que mudou de número recentemente e pede ajuda financeira.",
    "url_simulada": "https://wa.me/novo-contato-familia",
    "resposta_correta": "golpe",
    "explicacao": "Golpistas frequentemente se passam por familiares utilizando números desconhecidos.",
    "dica": "Confirme a identidade por outro canal.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Contato recente",
    "descricao": "Uma mensagem informa que existe uma oportunidade exclusiva disponível apenas naquele momento.",
    "url_simulada": "https://promocao-imediata-whats.site",
    "resposta_correta": "golpe",
    "explicacao": "A pressão para agir rapidamente é característica comum de golpes.",
    "dica": "Desconfie de urgência excessiva.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Confirmação de cadastro",
    "descricao": "Um contato solicita o código recebido por SMS para concluir uma verificação.",
    "url_simulada": "https://validacao-codigo-online.site",
    "resposta_correta": "golpe",
    "explicacao": "Códigos de verificação podem permitir acesso indevido à conta.",
    "dica": "Nunca compartilhe códigos recebidos por SMS.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Publicação compartilhada",
    "descricao": "Uma postagem promete distribuição gratuita de produtos mediante preenchimento de formulário.",
    "url_simulada": "https://cadastro-beneficio-gratis.site",
    "resposta_correta": "golpe",
    "explicacao": "Promessas exageradas costumam ser usadas para coletar dados pessoais.",
    "dica": "Analise a credibilidade da fonte.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Mensagem de suporte",
    "descricao": "Um perfil informa que houve um problema na conta e pede acesso a um link para correção.",
    "url_simulada": "https://suporte-instagram-online.net",
    "resposta_correta": "golpe",
    "explicacao": "Perfis falsos costumam simular equipes de suporte.",
    "dica": "Verifique se o perfil é realmente oficial.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Perfil institucional",
    "descricao": "Uma instituição publica orientações educativas em perfil verificado.",
    "url_simulada": "https://www.instagram.com/instituicaooficial",
    "resposta_correta": "seguro",
    "explicacao": "O perfil é oficial e não solicita dados pessoais.",
    "dica": "Observe a verificação do perfil.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Canal de comunicação",
    "descricao": "Uma empresa utiliza sua página oficial para divulgar informações públicas.",
    "url_simulada": "https://www.facebook.com/empresaoficial",
    "resposta_correta": "seguro",
    "explicacao": "A comunicação ocorre por canal institucional conhecido.",
    "dica": "Confira se o perfil é legítimo.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Aviso ao usuário",
    "descricao": "Uma organização compartilha recomendações de segurança digital em seu perfil oficial.",
    "url_simulada": "https://www.instagram.com/segurancaoficial",
    "resposta_correta": "seguro",
    "explicacao": "A publicação tem caráter educativo e não solicita informações.",
    "dica": "Observe o objetivo da mensagem.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Página oficial",
    "descricao": "Um perfil verificado publica atualizações sobre serviços oferecidos pela instituição.",
    "url_simulada": "https://www.linkedin.com/company/instituicaooficial",
    "resposta_correta": "seguro",
    "explicacao": "A comunicação ocorre em canal oficial da organização.",
    "dica": "Verifique a autenticidade do perfil.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Publicação informativa",
    "descricao": "Uma empresa divulga orientações para clientes sem solicitar dados pessoais.",
    "url_simulada": "https://www.instagram.com/empresaoficial",
    "resposta_correta": "seguro",
    "explicacao": "Não há solicitação de informações sensíveis.",
    "dica": "Observe se existem pedidos de dados.",
    "pontos": 10
},
{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Mensagem recebida",
    "descricao": "Um contato informa que existe um benefício disponível e apresenta um link para cadastro.",
    "url_simulada": "https://beneficio-acesso-rapido.site",
    "resposta_correta": "golpe",
    "explicacao": "O link direciona para uma página sem vínculo com qualquer instituição oficial.",
    "dica": "Observe o domínio apresentado.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Convite recebido",
    "descricao": "Uma mensagem convida você para participar de um grupo com ganhos financeiros garantidos.",
    "url_simulada": "https://grupo-renda-facil.net",
    "resposta_correta": "golpe",
    "explicacao": "Promessas de ganhos garantidos são frequentemente utilizadas por golpistas.",
    "dica": "Desconfie de lucro fácil.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Atualização de perfil",
    "descricao": "Uma mensagem informa que sua conta precisa ser validada e apresenta um link para confirmação.",
    "url_simulada": "https://validacao-perfil-online.site",
    "resposta_correta": "golpe",
    "explicacao": "O domínio não pertence à plataforma mencionada.",
    "dica": "Confira o endereço do site.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Contato comercial",
    "descricao": "Uma pessoa oferece produtos com preços muito abaixo do mercado e exige pagamento imediato.",
    "url_simulada": "https://oferta-unica-compras.shop",
    "resposta_correta": "golpe",
    "explicacao": "Preço extremamente baixo e urgência são sinais comuns de fraude.",
    "dica": "Compare os preços com outras lojas.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Mensagem privada",
    "descricao": "Um perfil desconhecido informa que você foi selecionado para receber um prêmio.",
    "url_simulada": "https://premio-especial-online.site",
    "resposta_correta": "golpe",
    "explicacao": "Prêmios inesperados são frequentemente usados como isca para golpes.",
    "dica": "Desconfie de benefícios não solicitados.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Suporte ao usuário",
    "descricao": "Um perfil envia mensagem oferecendo ajuda para recuperar sua conta.",
    "url_simulada": "https://recuperacao-conta-suporte.net",
    "resposta_correta": "golpe",
    "explicacao": "Perfis falsos costumam se passar por equipes de suporte.",
    "dica": "Procure os canais oficiais da plataforma.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Canal institucional",
    "descricao": "Uma organização publica comunicados e informações em perfil oficial verificado.",
    "url_simulada": "https://www.instagram.com/orgaooficial",
    "resposta_correta": "seguro",
    "explicacao": "A comunicação ocorre por um canal oficial da instituição.",
    "dica": "Observe a autenticidade do perfil.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Perfil corporativo",
    "descricao": "Uma empresa divulga seus serviços e canais de atendimento em perfil oficial.",
    "url_simulada": "https://www.facebook.com/empresaoficial",
    "resposta_correta": "seguro",
    "explicacao": "O perfil pertence à empresa e apresenta informações consistentes.",
    "dica": "Verifique a identidade da página.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Publicação educativa",
    "descricao": "Uma instituição compartilha recomendações de segurança para seus seguidores.",
    "url_simulada": "https://www.instagram.com/educacaooficial",
    "resposta_correta": "seguro",
    "explicacao": "A publicação possui caráter informativo e não solicita dados.",
    "dica": "Observe o objetivo da mensagem.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Canal de notícias",
    "descricao": "Uma organização divulga atualizações e comunicados por seu perfil oficial.",
    "url_simulada": "https://www.linkedin.com/company/organizacaooficial",
    "resposta_correta": "seguro",
    "explicacao": "A comunicação utiliza um canal institucional legítimo.",
    "dica": "Confira se o perfil é autêntico.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Perfil informativo",
    "descricao": "Uma página publica orientações ao público sem solicitar qualquer informação pessoal.",
    "url_simulada": "https://www.instagram.com/informacaooficial",
    "resposta_correta": "seguro",
    "explicacao": "Não há solicitação de dados nem redirecionamento suspeito.",
    "dica": "Observe o conteúdo da publicação.",
    "pontos": 10
},

{
    "assunto": "WhatsApp e redes sociais",
    "titulo": "Canal oficial",
    "descricao": "Uma empresa utiliza sua página oficial para divulgar avisos e novidades aos clientes.",
    "url_simulada": "https://www.facebook.com/marcaoficial",
    "resposta_correta": "seguro",
    "explicacao": "O canal pertence à empresa e não apresenta comportamento suspeito.",
    "dica": "Verifique a procedência da página.",
    "pontos": 10
},

    # PIX
    {
        "assunto": "Pix e pagamentos",
        "titulo": "Página de pagamento",
        "descricao": "Uma página informa que você foi selecionado para receber um prêmio, mas solicita pagamento de uma taxa via Pix.",
        "url_simulada": "https://liberar-premio-pix.site",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque cobra taxa antecipada para liberar um prêmio.",
        "dica": "Prêmio legítimo não exige taxa antecipada.",
        "pontos": 10
    },
    {
        "assunto": "Pix e pagamentos",
        "titulo": "Confirmação de pagamento",
        "descricao": "Um comprador envia imagem de comprovante Pix e solicita retirada imediata do produto.",
        "url_simulada": "https://comprovante-pix-enviado.com",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque comprovante em imagem pode ser falso. O saldo deve ser confirmado no banco.",
        "dica": "Confirme o dinheiro na conta.",
        "pontos": 10
    },
    {
        "assunto": "Pix e pagamentos",
        "titulo": "Pagamento por QR Code",
        "descricao": "Um QR Code está colado por cima de outro em um local público de pagamento.",
        "url_simulada": "qrcode://pagamento-alternativo",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque QR Codes adulterados podem direcionar pagamento para criminosos.",
        "dica": "Confira o nome do recebedor.",
        "pontos": 10
    },
    {
        "assunto": "Pix e pagamentos",
        "titulo": "Confirmação de pagamento",
        "descricao": "Antes de concluir o Pix, o usuário confere o nome do recebedor e o valor na tela do banco.",
        "url_simulada": "app://banco-pix-confirmacao",
        "resposta_correta": "seguro",
        "explicacao": "Conferir recebedor e valor antes de confirmar reduz o risco de erro ou golpe.",
        "dica": "Sempre revise os dados antes de confirmar.",
        "pontos": 10
    },
    {
    "assunto": "Pix e pagamentos",
    "titulo": "Solicitação de pagamento",
    "descricao": "Uma página informa que existe uma cobrança pendente e apresenta uma chave Pix para regularização.",
    "url_simulada": "https://regularizacao-financeira.net",
    "resposta_correta": "golpe",
    "explicacao": "O domínio não possui relação clara com a suposta cobrança apresentada.",
    "dica": "Verifique a origem da cobrança.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Comprovante recebido",
    "descricao": "Um comprador envia um comprovante em imagem e solicita liberação imediata do produto.",
    "url_simulada": "https://envio-comprovante-pagamento.site",
    "resposta_correta": "golpe",
    "explicacao": "Imagens de comprovantes podem ser adulteradas e não confirmam recebimento do valor.",
    "dica": "Confira o saldo na conta antes de entregar o produto.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Página de transferência",
    "descricao": "Uma página promete liberar um benefício após o envio de um Pix de confirmação.",
    "url_simulada": "https://confirmacao-beneficio-pix.net",
    "resposta_correta": "golpe",
    "explicacao": "Benefícios legítimos normalmente não exigem pagamento prévio.",
    "dica": "Desconfie de cobranças para liberar vantagens.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Código QR",
    "descricao": "Um QR Code é apresentado em uma página desconhecida para recebimento de uma vantagem financeira.",
    "url_simulada": "qrcode://recebimento-beneficio",
    "resposta_correta": "golpe",
    "explicacao": "O usuário não possui meios de validar o destinatário antes da leitura.",
    "dica": "Sempre confira quem receberá o pagamento.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Pagamento solicitado",
    "descricao": "Uma pessoa desconhecida informa que houve um erro e pede devolução imediata por Pix.",
    "url_simulada": "https://ajuste-pagamento-online.site",
    "resposta_correta": "golpe",
    "explicacao": "Golpistas utilizam histórias de engano para induzir transferências.",
    "dica": "Verifique a situação diretamente com o banco.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Confirmação bancária",
    "descricao": "O usuário verifica o nome do destinatário e o valor antes de concluir a transferência.",
    "url_simulada": "app://banco-confirmacao-pix",
    "resposta_correta": "seguro",
    "explicacao": "A conferência dos dados reduz significativamente o risco de erro.",
    "dica": "Sempre revise os dados da operação.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Transferência realizada",
    "descricao": "O pagamento é efetuado diretamente pelo aplicativo oficial do banco.",
    "url_simulada": "app://banco-oficial",
    "resposta_correta": "seguro",
    "explicacao": "O procedimento ocorre dentro do ambiente oficial da instituição financeira.",
    "dica": "Prefira sempre canais oficiais.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Pagamento eletrônico",
    "descricao": "O usuário confere cuidadosamente o CPF e o nome do recebedor antes de concluir a operação.",
    "url_simulada": "app://pix-verificacao",
    "resposta_correta": "seguro",
    "explicacao": "A validação dos dados do destinatário ajuda a evitar fraudes.",
    "dica": "Observe os dados do recebedor.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Transferência confirmada",
    "descricao": "Após realizar a operação, o usuário verifica o comprovante emitido pelo banco.",
    "url_simulada": "app://comprovante-bancario",
    "resposta_correta": "seguro",
    "explicacao": "O comprovante foi gerado pelo próprio aplicativo bancário.",
    "dica": "Utilize sempre o canal oficial.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Pagamento identificado",
    "descricao": "O destinatário foi validado e o valor conferido antes da confirmação da transação.",
    "url_simulada": "app://pix-seguro",
    "resposta_correta": "seguro",
    "explicacao": "A conferência prévia reduz a chance de golpes e erros.",
    "dica": "Revise os dados antes de confirmar.",
    "pontos": 10
},
{
    "assunto": "Pix e pagamentos",
    "titulo": "Solicitação recebida",
    "descricao": "Uma página informa que existe um valor disponível para saque após uma transferência de validação.",
    "url_simulada": "https://saque-validacao-pix.net",
    "resposta_correta": "golpe",
    "explicacao": "Transferências para liberar valores ou benefícios são características comuns de golpes.",
    "dica": "Desconfie de valores condicionados a pagamento prévio.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Cobrança apresentada",
    "descricao": "Uma página informa que existe uma pendência financeira e apresenta uma chave Pix para regularização imediata.",
    "url_simulada": "https://pendencia-financeira-online.site",
    "resposta_correta": "golpe",
    "explicacao": "Cobranças em domínios desconhecidos devem ser verificadas diretamente com a instituição.",
    "dica": "Confirme a cobrança por canais oficiais.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Pagamento solicitado",
    "descricao": "Uma pessoa informa que enviou dinheiro por engano e pede devolução imediata para outra chave Pix.",
    "url_simulada": "https://ajuste-financeiro.net",
    "resposta_correta": "golpe",
    "explicacao": "Golpistas utilizam histórias de transferência equivocada para induzir pagamentos.",
    "dica": "Verifique diretamente com seu banco.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Página de cadastro",
    "descricao": "Uma página informa que existe um benefício aguardando confirmação através de uma transferência Pix.",
    "url_simulada": "https://beneficio-confirmacao.site",
    "resposta_correta": "golpe",
    "explicacao": "Benefícios legítimos normalmente não exigem pagamentos prévios.",
    "dica": "Observe a lógica da solicitação.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Oferta recebida",
    "descricao": "Uma pessoa desconhecida promete retorno financeiro imediato após uma transferência.",
    "url_simulada": "https://ganho-imediato-pix.net",
    "resposta_correta": "golpe",
    "explicacao": "Promessas de retorno garantido após Pix são comuns em fraudes.",
    "dica": "Desconfie de lucro fácil.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Pagamento eletrônico",
    "descricao": "O usuário verifica cuidadosamente os dados do destinatário antes de concluir a operação.",
    "url_simulada": "app://pix-confirmacao",
    "resposta_correta": "seguro",
    "explicacao": "A conferência dos dados reduz o risco de fraude.",
    "dica": "Sempre confira quem receberá o valor.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Transferência bancária",
    "descricao": "O pagamento é realizado diretamente pelo aplicativo oficial da instituição financeira.",
    "url_simulada": "app://banco-oficial",
    "resposta_correta": "seguro",
    "explicacao": "O procedimento ocorre em ambiente controlado pelo banco.",
    "dica": "Utilize sempre canais oficiais.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Operação financeira",
    "descricao": "Antes de confirmar a transferência, o usuário revisa valor, CPF e nome do destinatário.",
    "url_simulada": "app://revisao-pix",
    "resposta_correta": "seguro",
    "explicacao": "A validação das informações aumenta a segurança da operação.",
    "dica": "Revise todos os dados antes de confirmar.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Confirmação de pagamento",
    "descricao": "O usuário verifica no extrato bancário que a operação foi concluída corretamente.",
    "url_simulada": "app://extrato-bancario",
    "resposta_correta": "seguro",
    "explicacao": "A confirmação é realizada diretamente pelo sistema bancário.",
    "dica": "Consulte o extrato quando houver dúvidas.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Transferência concluída",
    "descricao": "Após revisar todos os dados, o usuário conclui a operação utilizando aplicativo oficial.",
    "url_simulada": "app://pix-oficial",
    "resposta_correta": "seguro",
    "explicacao": "O processo segue boas práticas de segurança.",
    "dica": "Mantenha a conferência dos dados.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Pagamento realizado",
    "descricao": "O usuário confere a identidade do recebedor apresentada pelo banco antes da confirmação.",
    "url_simulada": "app://validacao-recebedor",
    "resposta_correta": "seguro",
    "explicacao": "A identificação do destinatário ajuda a evitar erros e golpes.",
    "dica": "Confira sempre o nome exibido.",
    "pontos": 10
},

{
    "assunto": "Pix e pagamentos",
    "titulo": "Operação concluída",
    "descricao": "Uma transferência é realizada após conferência completa dos dados e confirmação no aplicativo oficial.",
    "url_simulada": "app://operacao-segura",
    "resposta_correta": "seguro",
    "explicacao": "A operação segue um fluxo legítimo e seguro.",
    "dica": "Utilize sempre os aplicativos oficiais.",
    "pontos": 10
},

    # INVESTIMENTOS
    {
        "assunto": "Falsos investimentos",
        "titulo": "Anúncio de investimento",
        "descricao": "Uma página apresenta uma proposta para dobrar o valor investido em 7 dias com depósito via Pix.",
        "url_simulada": "https://renda-garantida-agora.com",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque promessa de retorno alto, rápido e garantido é sinal de fraude.",
        "dica": "Observe se há promessa de retorno garantido.",
        "pontos": 10
    },
    {
        "assunto": "Falsos investimentos",
        "titulo": "Anúncio patrocinado",
        "descricao": "Um anúncio usa imagem de uma celebridade dizendo que qualquer pessoa pode enriquecer rapidamente.",
        "url_simulada": "https://investimento-celebridade-ganhe.site",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque criminosos usam imagem de famosos para dar falsa credibilidade.",
        "dica": "Desconfie de promessas fáceis.",
        "pontos": 10
    },
    {
        "assunto": "Falsos investimentos",
        "titulo": "Convite para grupo",
        "descricao": "Um grupo apresenta lucros diários e pede depósito inicial para liberar o acesso.",
        "url_simulada": "https://grupo-vip-lucrodiario.net",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque investimentos reais envolvem risco e não prometem ganho certo.",
        "dica": "Promessa de lucro fixo é alerta.",
        "pontos": 10
    },
    {
        "assunto": "Falsos investimentos",
        "titulo": "Conteúdo financeiro",
        "descricao": "Uma página explica tipos de investimento, riscos e não promete retorno garantido.",
        "url_simulada": "https://www.educacaofinanceira.org",
        "resposta_correta": "seguro",
        "explicacao": "Conteúdo educativo e transparente sobre riscos não caracteriza golpe.",
        "dica": "Veja se há promessa garantida.",
        "pontos": 10
    },
    {
    "assunto": "Falsos investimentos",
    "titulo": "Plataforma financeira",
    "descricao": "Uma página informa que possui uma estratégia capaz de gerar ganhos consistentes em poucos dias.",
    "url_simulada": "https://resultado-financeiro-rapido.net",
    "resposta_correta": "golpe",
    "explicacao": "Promessas de ganhos elevados em curto prazo são características frequentes de fraudes.",
    "dica": "Observe se existem promessas exageradas.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Grupo de investidores",
    "descricao": "Uma comunidade promete retornos diários e apresenta resultados garantidos para todos os participantes.",
    "url_simulada": "https://grupo-renda-automatica.site",
    "resposta_correta": "golpe",
    "explicacao": "Investimentos legítimos envolvem risco e não oferecem lucro garantido.",
    "dica": "Desconfie de garantias absolutas.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Oportunidade financeira",
    "descricao": "Uma página afirma que um pequeno depósito pode multiplicar seu patrimônio rapidamente.",
    "url_simulada": "https://multiplicador-patrimonial.net",
    "resposta_correta": "golpe",
    "explicacao": "Promessas de multiplicação rápida de patrimônio são comuns em golpes.",
    "dica": "Compare a proposta com investimentos reais.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Consultoria financeira",
    "descricao": "Um suposto especialista garante lucro mensal fixo independentemente das condições do mercado.",
    "url_simulada": "https://consultoria-lucro-garantido.site",
    "resposta_correta": "golpe",
    "explicacao": "Nenhum investimento legítimo garante lucro fixo sem risco.",
    "dica": "Desconfie de promessas sem risco.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Plataforma de rendimento",
    "descricao": "Uma página informa que utiliza inteligência artificial para garantir ganhos automáticos.",
    "url_simulada": "https://ia-renda-garantida.net",
    "resposta_correta": "golpe",
    "explicacao": "Golpistas frequentemente utilizam termos tecnológicos para dar aparência de credibilidade.",
    "dica": "Observe se existe promessa de ganho garantido.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Portal educacional",
    "descricao": "Uma página apresenta conteúdos sobre investimentos e explica riscos associados a cada modalidade.",
    "url_simulada": "https://www.educacaofinanceira.org",
    "resposta_correta": "seguro",
    "explicacao": "O conteúdo possui caráter educativo e não promete retorno garantido.",
    "dica": "Observe se os riscos são apresentados.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Conteúdo financeiro",
    "descricao": "Uma plataforma explica conceitos de renda fixa, renda variável e gestão de risco.",
    "url_simulada": "https://www.financaseducativas.org",
    "resposta_correta": "seguro",
    "explicacao": "O foco está na educação financeira e não em promessas de lucro.",
    "dica": "Observe a finalidade do conteúdo.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Material informativo",
    "descricao": "Uma página apresenta diferentes alternativas de investimento e destaca possíveis riscos.",
    "url_simulada": "https://www.investimento-consciente.com.br",
    "resposta_correta": "seguro",
    "explicacao": "A transparência sobre riscos é característica positiva.",
    "dica": "Veja se existem alertas sobre riscos.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Portal de conhecimento",
    "descricao": "Uma instituição publica análises econômicas e materiais educativos para investidores.",
    "url_simulada": "https://www.educacaoeconomica.org.br",
    "resposta_correta": "seguro",
    "explicacao": "O conteúdo é informativo e não promete retorno financeiro.",
    "dica": "Observe se o objetivo é educar ou vender promessas.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Guia financeiro",
    "descricao": "Uma página explica diferentes perfis de investidor e estratégias de diversificação.",
    "url_simulada": "https://www.guiainvestidor.com.br",
    "resposta_correta": "seguro",
    "explicacao": "O conteúdo enfatiza planejamento e risco, sem promessas irreais.",
    "dica": "Investimentos legítimos normalmente discutem riscos.",
    "pontos": 10
},
{
    "assunto": "Falsos investimentos",
    "titulo": "Convite recebido",
    "descricao": "Uma página apresenta um grupo fechado que afirma possuir uma estratégia exclusiva de ganhos financeiros.",
    "url_simulada": "https://grupo-premium-renda.net",
    "resposta_correta": "golpe",
    "explicacao": "A proposta utiliza exclusividade e promessa de ganhos para atrair vítimas.",
    "dica": "Desconfie de promessas exclusivas e fáceis.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Plataforma online",
    "descricao": "Uma página informa que opera com criptomoedas e apresenta resultados consistentes para todos os usuários.",
    "url_simulada": "https://crypto-rendimento-global.site",
    "resposta_correta": "golpe",
    "explicacao": "Investimentos legítimos não garantem resultados para todos os participantes.",
    "dica": "Observe se há promessas de resultados garantidos.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Anúncio patrocinado",
    "descricao": "Uma publicidade apresenta depoimentos de pessoas que afirmam ter enriquecido rapidamente.",
    "url_simulada": "https://metodo-financeiro-imediato.net",
    "resposta_correta": "golpe",
    "explicacao": "Depoimentos isolados e promessas rápidas são comuns em fraudes.",
    "dica": "Analise se a promessa parece realista.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Área do investidor",
    "descricao": "Uma plataforma informa que utiliza um robô automático capaz de gerar ganhos previsíveis.",
    "url_simulada": "https://robo-lucroautomatico.site",
    "resposta_correta": "golpe",
    "explicacao": "A promessa de previsibilidade total não condiz com investimentos reais.",
    "dica": "Investimentos sempre envolvem risco.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Vídeo promocional",
    "descricao": "Uma pessoa conhecida aparece recomendando uma oportunidade financeira com retorno elevado.",
    "url_simulada": "https://investimento-exclusivo-famosos.net",
    "resposta_correta": "golpe",
    "explicacao": "Criminosos frequentemente utilizam imagens ou vídeos de terceiros para gerar credibilidade.",
    "dica": "Não confie apenas em quem aparece na propaganda.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Relatório financeiro",
    "descricao": "Uma página apresenta análises de mercado, cenários econômicos e riscos envolvidos nas aplicações.",
    "url_simulada": "https://www.analiseeconomica.org.br",
    "resposta_correta": "seguro",
    "explicacao": "O conteúdo possui caráter informativo e não promete ganhos garantidos.",
    "dica": "Observe se os riscos são discutidos.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Conteúdo educativo",
    "descricao": "Uma plataforma apresenta conceitos de planejamento financeiro e diversificação.",
    "url_simulada": "https://www.financasconscientes.com.br",
    "resposta_correta": "seguro",
    "explicacao": "O foco está na educação financeira.",
    "dica": "Observe se o objetivo é ensinar ou prometer ganhos.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Portal de análise",
    "descricao": "Uma página apresenta indicadores econômicos e notícias do mercado financeiro.",
    "url_simulada": "https://www.mercadoeconomico.com.br",
    "resposta_correta": "seguro",
    "explicacao": "O conteúdo é informativo e não oferece promessas financeiras.",
    "dica": "Observe a finalidade do portal.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Material de estudo",
    "descricao": "Uma instituição disponibiliza cursos gratuitos sobre investimentos e gestão de risco.",
    "url_simulada": "https://www.educacaofinanceira.org",
    "resposta_correta": "seguro",
    "explicacao": "O material possui finalidade educacional.",
    "dica": "Veja se existem explicações sobre riscos.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Página informativa",
    "descricao": "Uma organização explica diferentes modalidades de investimento e suas características.",
    "url_simulada": "https://www.investidorconsciente.org.br",
    "resposta_correta": "seguro",
    "explicacao": "O conteúdo apresenta informações sem promessas de retorno.",
    "dica": "Observe se há transparência nas informações.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Portal especializado",
    "descricao": "Uma página publica notícias, análises e estudos sobre economia e investimentos.",
    "url_simulada": "https://www.portalfinanceiro.com.br",
    "resposta_correta": "seguro",
    "explicacao": "O foco é a divulgação de informações financeiras.",
    "dica": "Verifique se existem promessas de lucro.",
    "pontos": 10
},

{
    "assunto": "Falsos investimentos",
    "titulo": "Biblioteca digital",
    "descricao": "Uma plataforma reúne materiais educativos sobre investimentos para iniciantes.",
    "url_simulada": "https://www.aprendainvestir.org.br",
    "resposta_correta": "seguro",
    "explicacao": "O conteúdo possui caráter educativo e não comercial.",
    "dica": "Observe a finalidade da plataforma.",
    "pontos": 10
},

    # DADOS PESSOAIS
    {
        "assunto": "Golpes com dados pessoais",
        "titulo": "Regularização cadastral",
        "descricao": "Mensagem pede CPF, nome da mãe e foto do documento para concluir uma regularização.",
        "url_simulada": "https://regulariza-cpf-online.net",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque solicita dados sensíveis em domínio não oficial.",
        "dica": "Não envie documentos por páginas não verificadas.",
        "pontos": 10
    },
    {
        "assunto": "Golpes com dados pessoais",
        "titulo": "Cadastro de oportunidade",
        "descricao": "Um formulário apresenta uma oportunidade de emprego e solicita foto do documento, CPF e dados bancários.",
        "url_simulada": "https://vaga-emprego-imediato.site",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque vagas falsas podem ser usadas para roubar dados pessoais.",
        "dica": "Pesquise a empresa antes de enviar documentos.",
        "pontos": 10
    },
    {
        "assunto": "Golpes com dados pessoais",
        "titulo": "Pesquisa online",
        "descricao": "Uma página apresenta uma pesquisa com brinde e solicita dados pessoais completos.",
        "url_simulada": "https://pesquisa-premiada-dados.net",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque usa promessa de brinde para coletar dados sensíveis.",
        "dica": "Evite fornecer dados desnecessários.",
        "pontos": 10
    },
    {
        "assunto": "Golpes com dados pessoais",
        "titulo": "Portal de serviços",
        "descricao": "O usuário acessa um portal digitando o endereço e utilizando autenticação segura.",
        "url_simulada": "https://www.gov.br",
        "resposta_correta": "seguro",
        "explicacao": "O acesso direto a portal oficial reduz o risco de páginas falsas.",
        "dica": "Digite o endereço oficial.",
        "pontos": 10
    },
    {
    "assunto": "Golpes com dados pessoais",
    "titulo": "Atualização cadastral",
    "descricao": "Uma página informa que alguns dados precisam ser confirmados para manter o acesso a um serviço.",
    "url_simulada": "https://confirmacao-cadastro-online.net",
    "resposta_correta": "golpe",
    "explicacao": "O domínio não possui relação clara com a instituição mencionada e solicita informações sensíveis.",
    "dica": "Verifique o domínio antes de informar dados.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Formulário disponível",
    "descricao": "Uma página apresenta um cadastro solicitando CPF, RG e fotografia do documento.",
    "url_simulada": "https://cadastro-validacao-cliente.site",
    "resposta_correta": "golpe",
    "explicacao": "A coleta de documentos em ambiente não verificado representa risco de fraude.",
    "dica": "Observe quem está solicitando os documentos.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Cadastro online",
    "descricao": "Uma página informa que existe uma oportunidade disponível mediante preenchimento de dados completos.",
    "url_simulada": "https://registro-beneficio-online.net",
    "resposta_correta": "golpe",
    "explicacao": "Golpistas frequentemente utilizam formulários para coletar informações pessoais.",
    "dica": "Avalie a legitimidade do serviço.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Solicitação recebida",
    "descricao": "Uma página solicita fotografia segurando um documento para concluir uma validação.",
    "url_simulada": "https://validacao-identidade-digital.site",
    "resposta_correta": "golpe",
    "explicacao": "Documentos e selfies podem ser utilizados em fraudes de identidade.",
    "dica": "Confirme se a instituição é legítima.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Regularização de cadastro",
    "descricao": "Uma página informa que existe uma inconsistência cadastral e solicita atualização imediata.",
    "url_simulada": "https://regularizacao-documentos.net",
    "resposta_correta": "golpe",
    "explicacao": "A combinação de urgência e solicitação de dados é comum em golpes.",
    "dica": "Desconfie de mensagens que pressionam decisões rápidas.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Portal de serviços",
    "descricao": "O usuário acessa diretamente um portal oficial utilizando autenticação conhecida.",
    "url_simulada": "https://www.gov.br",
    "resposta_correta": "seguro",
    "explicacao": "O acesso ocorre em ambiente oficial e conhecido pelo usuário.",
    "dica": "Prefira digitar o endereço manualmente.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Área do cidadão",
    "descricao": "O usuário acessa um serviço oficial através do domínio principal da instituição.",
    "url_simulada": "https://www.gov.br",
    "resposta_correta": "seguro",
    "explicacao": "O domínio pertence ao portal oficial.",
    "dica": "Observe o endereço principal.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Serviço digital",
    "descricao": "Uma plataforma oficial solicita autenticação antes de permitir acesso às informações.",
    "url_simulada": "https://www.gov.br",
    "resposta_correta": "seguro",
    "explicacao": "A autenticação faz parte do procedimento legítimo do serviço.",
    "dica": "Observe se o domínio é oficial.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Consulta cadastral",
    "descricao": "O usuário acessa diretamente um serviço conhecido para consultar informações pessoais.",
    "url_simulada": "https://www.gov.br",
    "resposta_correta": "seguro",
    "explicacao": "A consulta é realizada em ambiente legítimo.",
    "dica": "Prefira acessar serviços oficiais diretamente.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Portal institucional",
    "descricao": "Uma plataforma apresenta informações públicas e acesso autenticado para seus usuários.",
    "url_simulada": "https://www.gov.br",
    "resposta_correta": "seguro",
    "explicacao": "O serviço opera em domínio oficial e reconhecido.",
    "dica": "Confira o endereço antes de inserir informações.",
    "pontos": 10
},
{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Cadastro complementar",
    "descricao": "Uma página informa que alguns dados adicionais são necessários para concluir um processo em andamento.",
    "url_simulada": "https://complemento-cadastral-online.site",
    "resposta_correta": "golpe",
    "explicacao": "O domínio não possui relação clara com uma instituição legítima.",
    "dica": "Observe quem solicita os dados.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Validação de identidade",
    "descricao": "Uma página informa que uma verificação é necessária para evitar restrições futuras.",
    "url_simulada": "https://validacao-identidade-cliente.net",
    "resposta_correta": "golpe",
    "explicacao": "A solicitação ocorre em domínio desconhecido.",
    "dica": "Confira se o endereço pertence à instituição.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Atualização de informações",
    "descricao": "Uma página apresenta um formulário solicitando informações pessoais e documentos.",
    "url_simulada": "https://dados-atualizacao-segura.site",
    "resposta_correta": "golpe",
    "explicacao": "A coleta de dados sensíveis ocorre em ambiente não verificado.",
    "dica": "Analise a credibilidade do site.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Solicitação online",
    "descricao": "Uma página informa que um benefício depende da confirmação imediata dos dados do usuário.",
    "url_simulada": "https://beneficio-confirmacao-cadastro.net",
    "resposta_correta": "golpe",
    "explicacao": "A urgência é utilizada para induzir o compartilhamento de dados.",
    "dica": "Desconfie de pressões por rapidez.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Processo de validação",
    "descricao": "Uma página solicita envio de documentos para concluir uma análise cadastral.",
    "url_simulada": "https://analise-documental-online.site",
    "resposta_correta": "golpe",
    "explicacao": "Documentos pessoais podem ser utilizados em fraudes de identidade.",
    "dica": "Confirme a autenticidade da solicitação.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Área de serviços",
    "descricao": "O usuário acessa diretamente um portal governamental conhecido para consultar informações.",
    "url_simulada": "https://www.gov.br",
    "resposta_correta": "seguro",
    "explicacao": "O acesso é realizado em domínio oficial.",
    "dica": "Observe o endereço principal.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Consulta autenticada",
    "descricao": "O acesso ao sistema exige autenticação e ocorre em ambiente oficial.",
    "url_simulada": "https://www.gov.br",
    "resposta_correta": "seguro",
    "explicacao": "O procedimento ocorre dentro do portal legítimo.",
    "dica": "Verifique sempre o domínio.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Portal de atendimento",
    "descricao": "O usuário acessa um serviço institucional digitando manualmente o endereço no navegador.",
    "url_simulada": "https://www.gov.br",
    "resposta_correta": "seguro",
    "explicacao": "O acesso direto reduz riscos de redirecionamento.",
    "dica": "Prefira digitar o endereço manualmente.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Consulta pública",
    "descricao": "Uma plataforma oficial disponibiliza informações e serviços autenticados aos usuários.",
    "url_simulada": "https://www.gov.br",
    "resposta_correta": "seguro",
    "explicacao": "O domínio pertence ao governo federal.",
    "dica": "Observe o endereço completo.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Serviço institucional",
    "descricao": "O usuário consulta informações pessoais em ambiente oficial já conhecido.",
    "url_simulada": "https://www.gov.br",
    "resposta_correta": "seguro",
    "explicacao": "O serviço utiliza domínio legítimo.",
    "dica": "Confira o endereço antes de inserir dados.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Área do cidadão",
    "descricao": "Uma plataforma governamental oferece autenticação para acesso a informações pessoais.",
    "url_simulada": "https://www.gov.br",
    "resposta_correta": "seguro",
    "explicacao": "O acesso ocorre em ambiente oficial e reconhecido.",
    "dica": "Observe o domínio utilizado.",
    "pontos": 10
},

{
    "assunto": "Golpes com dados pessoais",
    "titulo": "Portal digital",
    "descricao": "O usuário acessa um serviço público através de endereço oficial conhecido.",
    "url_simulada": "https://www.gov.br",
    "resposta_correta": "seguro",
    "explicacao": "O serviço utiliza infraestrutura oficial.",
    "dica": "Confira sempre o domínio antes de informar dados.",
    "pontos": 10
},

    # IA / DEEPFAKE
    {
        "assunto": "Golpes com dados pessoais",
        "titulo": "Mensagem de áudio",
        "descricao": "Você recebe um áudio parecido com a voz de um familiar pedindo uma transferência.",
        "url_simulada": "audio://pedido-familiar",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque criminosos podem usar clonagem de voz para simular pessoas conhecidas.",
        "dica": "Confirme por outro canal antes de agir.",
        "pontos": 10
    },
    {
        "assunto": "Falsos investimentos",
        "titulo": "Vídeo promocional",
        "descricao": "Um vídeo mostra uma pessoa famosa recomendando uma plataforma de investimento.",
        "url_simulada": "https://video-investimento-garantido.site",
        "resposta_correta": "golpe",
        "explicacao": "É golpe porque vídeos manipulados podem ser usados para promover fraudes financeiras.",
        "dica": "Desconfie de celebridades prometendo lucro.",
        "pontos": 10
    },
    {
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Mensagem de áudio",
    "descricao": "Você recebe um áudio de uma pessoa conhecida solicitando uma transferência com urgência.",
    "url_simulada": "audio://contato-conhecido",
    "resposta_correta": "golpe",
    "explicacao": "Clonagem de voz pode ser utilizada para simular familiares ou conhecidos.",
    "dica": "Confirme a solicitação por outro canal.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Vídeo recebido",
    "descricao": "Um vídeo mostra uma pessoa conhecida recomendando uma oportunidade financeira.",
    "url_simulada": "https://oportunidade-financeira-ia.net",
    "resposta_correta": "golpe",
    "explicacao": "Vídeos manipulados podem ser utilizados para aumentar a credibilidade de golpes.",
    "dica": "Não confie apenas na imagem apresentada.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Contato profissional",
    "descricao": "Uma mensagem afirma ser enviada pelo diretor da empresa e solicita uma transferência imediata.",
    "url_simulada": "https://mensagem-diretoria-online.site",
    "resposta_correta": "golpe",
    "explicacao": "Golpes do falso chefe utilizam pressão e autoridade para convencer a vítima.",
    "dica": "Confirme diretamente com a pessoa.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Convite recebido",
    "descricao": "Uma pessoa desconhecida inicia uma conversa utilizando fotos extremamente realistas e solicita informações pessoais.",
    "url_simulada": "https://perfil-social-conexao.net",
    "resposta_correta": "golpe",
    "explicacao": "Perfis gerados por IA podem ser utilizados para engenharia social.",
    "dica": "Desconfie de contatos que pedem dados rapidamente.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Videochamada",
    "descricao": "Uma chamada apresenta uma pessoa conhecida solicitando dados bancários para resolver um problema urgente.",
    "url_simulada": "video://chamada-urgente",
    "resposta_correta": "golpe",
    "explicacao": "Deepfakes podem ser utilizados em chamadas para simular identidades.",
    "dica": "Confirme a situação por outro meio.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Canal oficial",
    "descricao": "Uma instituição publica orientações sobre uso responsável de inteligência artificial.",
    "url_simulada": "https://www.gov.br",
    "resposta_correta": "seguro",
    "explicacao": "O conteúdo possui caráter educativo e está em domínio oficial.",
    "dica": "Observe a origem da informação.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Material educativo",
    "descricao": "Uma universidade disponibiliza conteúdo explicando riscos de deepfakes e desinformação.",
    "url_simulada": "https://www.universidade.edu.br",
    "resposta_correta": "seguro",
    "explicacao": "O objetivo é informar e educar o usuário.",
    "dica": "Observe a finalidade do conteúdo.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Portal acadêmico",
    "descricao": "Uma instituição apresenta estudos e pesquisas sobre inteligência artificial.",
    "url_simulada": "https://www.pesquisaia.org.br",
    "resposta_correta": "seguro",
    "explicacao": "O conteúdo possui caráter científico e informativo.",
    "dica": "Verifique a credibilidade da instituição.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Página informativa",
    "descricao": "Uma organização publica recomendações para identificar conteúdos manipulados digitalmente.",
    "url_simulada": "https://www.segurancadigital.org.br",
    "resposta_correta": "seguro",
    "explicacao": "O material é educativo e não solicita dados pessoais.",
    "dica": "Observe se existe pedido de informações.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Conteúdo educativo",
    "descricao": "Uma plataforma apresenta exemplos de golpes modernos envolvendo inteligência artificial.",
    "url_simulada": "https://www.educacao-digital.org",
    "resposta_correta": "seguro",
    "explicacao": "A finalidade é conscientização e prevenção.",
    "dica": "Observe se há tentativa de obter dados ou dinheiro.",
    "pontos": 10
},
{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Chamada recebida",
    "descricao": "Uma ligação utiliza uma voz muito parecida com a de um familiar solicitando ajuda financeira.",
    "url_simulada": "audio://ligacao-familiar",
    "resposta_correta": "golpe",
    "explicacao": "Criminosos podem utilizar clonagem de voz para simular pessoas conhecidas.",
    "dica": "Confirme por outro canal.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Contato corporativo",
    "descricao": "Uma mensagem informa que um superior precisa de uma transferência urgente para resolver um problema.",
    "url_simulada": "https://diretoria-empresa-online.site",
    "resposta_correta": "golpe",
    "explicacao": "Golpes de engenharia social exploram autoridade e urgência.",
    "dica": "Confirme diretamente com a pessoa.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Perfil profissional",
    "descricao": "Uma pessoa recém-adicionada afirma possuir uma oportunidade exclusiva e solicita informações pessoais.",
    "url_simulada": "https://network-profissional-online.net",
    "resposta_correta": "golpe",
    "explicacao": "Perfis falsos podem ser usados para coleta de dados.",
    "dica": "Pesquise a identidade do contato.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Videochamada recebida",
    "descricao": "Uma pessoa conhecida solicita dados bancários durante uma chamada com qualidade de imagem incomum.",
    "url_simulada": "video://contato-conhecido",
    "resposta_correta": "golpe",
    "explicacao": "Deepfakes podem ser utilizados para simular pessoas reais.",
    "dica": "Nunca forneça dados sensíveis sem confirmação.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Mensagem automatizada",
    "descricao": "Um sistema informa que detectou um problema e solicita confirmação imediata de dados financeiros.",
    "url_simulada": "https://seguranca-automatica-cliente.net",
    "resposta_correta": "golpe",
    "explicacao": "Automação e IA podem ser usadas para aumentar a escala dos golpes.",
    "dica": "Verifique o canal oficial.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Atendimento virtual",
    "descricao": "Um assistente virtual solicita senha completa para validar a identidade do usuário.",
    "url_simulada": "https://assistente-validacao-online.site",
    "resposta_correta": "golpe",
    "explicacao": "Serviços legítimos não pedem senhas completas.",
    "dica": "Nunca informe senhas.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Convite especial",
    "descricao": "Uma mensagem personalizada apresenta informações sobre você e oferece uma oportunidade financeira exclusiva.",
    "url_simulada": "https://convite-premium-investidor.net",
    "resposta_correta": "golpe",
    "explicacao": "IA pode ser utilizada para personalizar golpes e aumentar a credibilidade.",
    "dica": "Desconfie de ofertas excessivamente personalizadas.",
    "pontos": 10
},
{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Portal informativo",
    "descricao": "Uma instituição publica orientações sobre como identificar conteúdos manipulados digitalmente.",
    "url_simulada": "https://www.segurancadigital.org.br",
    "resposta_correta": "seguro",
    "explicacao": "O conteúdo possui finalidade educativa e não solicita dados pessoais.",
    "dica": "Observe se há pedidos de informações ou pagamentos.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Curso online",
    "descricao": "Uma universidade disponibiliza material explicando riscos relacionados a inteligência artificial e desinformação.",
    "url_simulada": "https://www.universidade.edu.br",
    "resposta_correta": "seguro",
    "explicacao": "O objetivo é educacional e preventivo.",
    "dica": "Verifique a instituição responsável.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Biblioteca digital",
    "descricao": "Uma plataforma reúne pesquisas e estudos sobre tecnologias de inteligência artificial.",
    "url_simulada": "https://www.pesquisaia.org.br",
    "resposta_correta": "seguro",
    "explicacao": "O conteúdo possui caráter acadêmico e informativo.",
    "dica": "Observe a finalidade da plataforma.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Central de conhecimento",
    "descricao": "Uma organização apresenta exemplos de golpes modernos e formas de prevenção.",
    "url_simulada": "https://www.educacao-digital.org",
    "resposta_correta": "seguro",
    "explicacao": "A finalidade é conscientização dos usuários.",
    "dica": "Veja se existe tentativa de obter dados ou dinheiro.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Material educativo",
    "descricao": "Uma página apresenta recomendações para verificar autenticidade de vídeos e áudios recebidos.",
    "url_simulada": "https://www.verificacaodigital.org.br",
    "resposta_correta": "seguro",
    "explicacao": "O conteúdo é educativo e voltado para prevenção.",
    "dica": "Observe a finalidade da informação.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Portal de pesquisa",
    "descricao": "Uma instituição divulga estudos sobre segurança digital e inteligência artificial.",
    "url_simulada": "https://www.inovacaodigital.edu.br",
    "resposta_correta": "seguro",
    "explicacao": "A plataforma possui caráter informativo e acadêmico.",
    "dica": "Verifique quem mantém o portal.",
    "pontos": 10
},

{
    "assunto": "IA, Deepfake e Engenharia Social",
    "titulo": "Página institucional",
    "descricao": "Uma organização publica recomendações para evitar golpes envolvendo clonagem de voz.",
    "url_simulada": "https://www.prevencaogolpes.org.br",
    "resposta_correta": "seguro",
    "explicacao": "O objetivo é orientar usuários sobre riscos digitais.",
    "dica": "Analise se há pedido de dados ou pagamentos.",
    "pontos": 10
}

]


def get_assunto_id(cursor, nome):
    p = placeholder()
    cursor.execute(f"SELECT id FROM assuntos WHERE nome = {p}", (nome,))
    assunto = fetchone(cursor)
    return assunto["id"] if assunto else None
def misturar_dominios():
    substituicoes = {
        "https://www.bancooficial.com.br": "https://www.bancoexemplo.com.br",
        "app://banco-oficial": "app://banco-exemplo-oficial",
        "https://www.correios.com.br": "https://www.correios.com.br",
        "https://www.gov.br": "https://www.gov.br",

        "https://www.servicooficial.com": "https://www.servicoexemplo.com.br",
        "https://www.empresaoficial.com.br": "https://www.empresaexemplo.com.br",
        "https://www.plataformaoficial.com.br": "https://www.plataformaexemplo.com.br",

        "https://www.marketplaceconfiavel.com.br": "https://www.mercadoexemplo.com.br",
        "https://www.lojaconhecida.com.br": "https://www.lojaexemplo.com.br",
        "https://www.lojasegura.com.br": "https://www.lojaverificada.com.br",

        "https://megaoferta-celular.shop": "https://mega-oferta-celular.vip",
        "https://superdesconto-total.site": "https://superdesconto-total.online",
        "https://games-promocao-relampago.shop": "https://games-promocao24h.store",

        "https://correios-taxas-entrega.net": "https://correios-taxas-entrega.info",
        "https://reagendar-entrega-correios.site": "https://reagendar-entrega-brasil.online",
        "https://taxa-alfandega-entrega.net": "https://minha-entrega-alfandega.com",

        "https://premio-especial-whatsapp.site": "https://premio-especial-brasil.club",
        "https://validacao-codigo-online.site": "https://validacao-codigo24h.online",

        "https://renda-garantida-agora.com": "https://renda-garantida24h.vip",
        "https://crypto-rendimento-global.site": "https://crypto-rendimento-global.online",
        "https://robo-lucroautomatico.site": "https://robo-investidor-premium.com",

        "https://regulariza-cpf-online.net": "https://regulariza-cadastro-brasil.info",
        "https://cadastro-validacao-cliente.site": "https://validacao-documental-online.com",
    }

    for q in QUESTOES:
        if q["url_simulada"] in substituicoes:
            q["url_simulada"] = substituicoes[q["url_simulada"]]

def seed_questoes():

    create_database()
    misturar_dominios()

    conn = get_connection()
    cursor = conn.cursor()
    p = placeholder()


    print("Iniciando seed de questões...")


    inseridas = 0


    for q in QUESTOES:

        assunto_id = get_assunto_id(cursor, q["assunto"])


        if assunto_id is None:

            print(f"Assunto não encontrado: {q['assunto']}")
            continue


        cursor.execute(
            f"""
            SELECT id FROM questoes
            WHERE titulo = {p}
            AND descricao = {p}
            AND url_simulada = {p}
            """,
            (
                q["titulo"],
                q["descricao"],
                q["url_simulada"]
            )
        )


        existente = fetchone(cursor)


        if existente:
            continue


        cursor.execute(
            f"""
            INSERT INTO questoes
            (
                titulo,
                descricao,
                url_simulada,
                resposta_correta,
                explicacao,
                dica,
                pontos,
                assunto_id
            )
            VALUES
            ({p},{p},{p},{p},{p},{p},{p},{p})
            """,
            (
                q["titulo"],
                q["descricao"],
                q["url_simulada"],
                q["resposta_correta"],
                q["explicacao"],
                q["dica"],
                q["pontos"],
                assunto_id
            )
        )

        inseridas += 1


conn.commit()

    # =====================
    # TESTE DO BANCO REAL
    # =====================

    cursor.execute("SELECT COUNT(*) AS total FROM questoes")
    linha = fetchone(cursor)
    print(
        "BANCO REAL - QUESTÕES:",
        dict(linha) if not isinstance(linha, dict) else linha
    )

    cursor.execute("SELECT COUNT(*) AS total FROM assuntos")
    linha = fetchone(cursor)
    print(
        "BANCO REAL - ASSUNTOS:",
        dict(linha) if not isinstance(linha, dict) else linha
    )


    conn.close()

    print("SEED FINALIZADO COM SUCESSO!")

if __name__ == "__main__":
    seed_questoes()