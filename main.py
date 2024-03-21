import pandas as pd
import plotly_express as px
import xlsxwriter

dados = pd.read_excel(r'D:\Projetos\Intensivão-Python\Pandas\vendas.xlsx') #Lendo a planilha
cabecalho = dados.head()
dados_info = dados.info()
tailsDados = dados.tail()
#preco_descritivos = dados.preco.describe().to_frame() #dá pra trocar to_frame por to_excel
#object_plan = pd.Index([2,9]).to_frame(name='Colunas').transpose() 
#print(object_plan)
lojas = dados.loja.describe().to_frame
lojas_qtd_vendas = dados.loja.value_counts().to_frame()
#dados_forma_de_pagamento = dados.forma_pagamentos.value_counts().to_frame()
dados_agrupado_faturamento_de_lojas = dados.groupby("loja").preco.sum().to_frame()
faturamento_por_estados_e_cidades = dados.groupby(["estado", "cidade"]).preco.sum().to_frame()

grafico = px.histogram(
             dados, 
             x="loja", 
             y="preco",
             text_auto=True, 
             title="Faturamento por loja",
             color = "forma_pagamento",
             )
grafico.show()
grafico.write_html("grafico_faturamento.html")

colunas = ['loja', 'cidade', 'estado', 'local_consumo']
for coluna in colunas:
    grafico = px.histogram(
             dados, 
             x="loja", 
             y="preco",
             text_auto=True, 
             title=f"""Faturamento por Localidade""",
             color = "forma_pagamento",
             )
    grafico.show()
    grafico.write_html('Colunas do grafico.html')

#print(dados, cabecalho, dados_info, preco_descritivos, lojas, lojas_qtd_vendas, dados_forma_de_pagamento, dados_agrupado_faturamento_de_lojas, faturamento_por_estados_e_cidades)

