# Conteúdo do site da Eko Dental.
# Edite aqui e rode `python3 _fonte/gerar_site.py` na raiz do repositório.

CLINICA = {
    "nome": "Eko Dental",
    "whatsapp": "5583999843311",
    "telefone_exibicao": "(83) 99984-3311",
    "rua": "Av. Valdemar Naziazeno, 940",
    "bairro": "Ernesto Geisel",
    "bairro_curto": "Geisel",
    "cidade": "João Pessoa",
    "uf": "PB",
    "cep": "58075-000",
    "rt_nome": "Dra. Caroline Chaves",
    "rt_cargo": "Cirurgiã-dentista",
    "rt_cro": "CRO-PB 6742",
    "horario_curto": "Seg a sex, 8h às 18h · Sáb, 9h às 12h",
    "url_base": "https://ekoversobr.github.io/ekodental/",
    "gtm": "GTM-P57ZS496",
    "logo": "logo-eko-dental.png",
}

TRATAMENTOS = [
    {"slug": "sedacao-consciente", "nome": "Sedação consciente", "servico_msg": "sedação consciente",
     "h1": "Sedação consciente no Geisel",
     "sub": "Para quem tem medo de dentista: você fica relaxado e acordado durante o tratamento.",
     "description": "Sedação consciente no Geisel, João Pessoa. Agende sua avaliação na Eko Dental pelo WhatsApp."},
    {"slug": "implantes-dentarios", "nome": "Implantes dentários", "servico_msg": "implante dentário",
     "h1": "Implante dentário no Geisel",
     "sub": "Reponha dentes perdidos com uma solução fixa. O plano e o orçamento saem na avaliação.",
     "description": "Implante dentário no Geisel, João Pessoa. Agende sua avaliação na Eko Dental pelo WhatsApp."},
    {"slug": "tratamento-de-canal", "nome": "Tratamento de canal", "servico_msg": "tratamento de canal",
     "h1": "Tratamento de canal no Geisel",
     "sub": "Trate o dente por dentro e mantenha o seu dente natural.",
     "description": "Tratamento de canal no Geisel, João Pessoa. Agende sua avaliação na Eko Dental pelo WhatsApp."},
    {"slug": "extracao-de-siso", "nome": "Extração de siso", "servico_msg": "extração de siso",
     "h1": "Extração de siso no Geisel",
     "sub": "Siso doendo ou sem espaço para nascer? Com opção de sedação consciente.",
     "description": "Extração de siso no Geisel, João Pessoa, com opção de sedação consciente. Agende pelo WhatsApp."},
    {"slug": "facetas-em-resina", "nome": "Facetas em resina", "servico_msg": "facetas em resina",
     "h1": "Facetas em resina no Geisel",
     "sub": "Ajuste cor, formato e pequenos espaços dos dentes da frente.",
     "description": "Facetas em resina no Geisel, João Pessoa. Agende sua avaliação na Eko Dental pelo WhatsApp."},
]

# Mensagem dos botões da página principal (o site acrescenta o código de atendimento no fim).
MSG_HOME = ("Olá, tudo bem? Cliquei no anúncio da Eko Dental no Google, fui ao site e cliquei "
            "no botão do WhatsApp e gostaria de mais informações.")

# Endereços antigos (versão anterior do site, ainda usados em anúncios e sitelinks)
# que passam a redirecionar para as páginas novas. "" = página principal.
REDIRECIONAMENTOS = {
    "agendamento.html": "",
    "clinica.html": "",
    "contato.html": "",
    "servicos.html": "",
    "implante-dentario.html": "implantes-dentarios/",
    "sedacao-consciente.html": "sedacao-consciente/",
    "sedacao-infantil.html": "sedacao-consciente/",
    "tratamento-de-canal.html": "tratamento-de-canal/",
    "extracao-de-siso.html": "extracao-de-siso/",
    "facetas-em-resina.html": "facetas-em-resina/",
    "aparelhos-ortodonticos.html": "",
    "odontopediatria.html": "",
    "limpeza-dental.html": "",
    "clareamento-dental.html": "",
}
