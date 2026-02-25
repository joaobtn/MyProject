# 1. Dados do Usuário
from datetime import date


nome_func = "João Silva"
cargo = "Analista de Dados"
empresa = "Tech Solutions Ltda"
data_hoje = date.today().strftime("%d/%m/%Y")
cumprir_aviso = True # Mude para False se for saída imediata

# 2. Lógica do Aviso Prévio
aviso_texto = "cumprirei o aviso prévio trabalhado" if cumprir_aviso else "não cumprirei o aviso prévio, solicitando a dispensa"

# 3. Gerar a Carta
carta = f"""
À {empresa}

Prezados,

Por meio desta carta, comunico formalmente meu pedido de demissão do cargo de {cargo}.

Informo que {aviso_texto}, conforme as orientações do RH e as normas da CLT. Meu último dia de trabalho será em 30 dias a partir desta data, ou conforme acordado.

Agradeço a oportunidade de crescimento profissional durante este período.

Atenciosamente,

__________________________________________
{nome_func}
{data_hoje}
"""

print(carta)