# Eko Dental: site

Site estático da Eko Dental (odontologia no Geisel, João Pessoa), publicado pelo GitHub Pages em https://ekoversobr.github.io/ekodental/. Gerenciado pela Ekoverso.

## Páginas
| Endereço | Uso |
|---|---|
| `/` | Página principal: dentista no Geisel |
| `/sedacao-consciente/` | Sedação consciente |
| `/implantes-dentarios/` | Implantes |
| `/tratamento-de-canal/` | Tratamento de canal |
| `/extracao-de-siso/` | Extração de siso |
| `/facetas-em-resina/` | Facetas em resina |
| `/privacidade/` | Política de privacidade (LGPD) |
| `/*.html` antigos (agendamento, implante-dentario, sedacao-consciente, etc.) | Endereços da versão anterior, redirecionam para as páginas novas mantendo o gclid |

## Como editar
Os textos ficam em `_fonte/conteudo.py`. Depois de editar, rode na raiz:

```
python3 _fonte/gerar_site.py
```

O script reescreve todos os HTML. Não edite os HTML gerados à mão: a próxima geração apaga a mudança. Estilos em `assets/site.css`, comportamento em `assets/site.js`.

Ao trocar de domínio, mude `url_base` em `_fonte/conteudo.py` e gere de novo.

## Mensuração
- Google Tag Manager `GTM-P57ZS496` (contêiner da Eko Dental) em todas as páginas. Nele, a conversão do Google Ads "Contato - Botão WPP" dispara no clique em links `wa.me`. Ela mede intenção de contato, não conversa nem venda.
- `assets/site.js` gera um código de atendimento (ex.: ED7F3K, sempre começa com ED) para quem chega por anúncio do Google (`gclid`) e coloca esse código no fim da mensagem do WhatsApp. Envia também o evento `whatsapp_click` ao dataLayer.
- Com `ENDPOINT` preenchido em `assets/site.js`, o par código + GCLID vai para a aba "Cliques do site" da planilha "Ekoverso | Eko Dental – Controle de Leads e Vendas (Google Ads)" (script em `_fonte/apps-script-planilha.gs`). A equipe anota o código do paciente na planilha, e agendamentos e vendas voltam ao Google Ads como conversões offline.
- Enquanto `ENDPOINT` estiver vazio, o código continua indo na mensagem do WhatsApp, mas o GCLID não é gravado na planilha.

## Regras de conteúdo
- Publicidade odontológica: manter nome e CRO da responsável técnica em todas as páginas. Não anunciar preços, descontos ou promessas de resultado.
- Não pedir dados de saúde em formulários ou URLs, nem enviá-los a ferramentas de anúncio ou analytics.
