#imports necessarios para o uso/exibição do DashBoard
import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")

#Link do Arquivo CSV(Tabela)
df = pd.read_csv('dado.csv', encoding='latin1')
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

#Definição de Ano + Mês 
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]
#df_filtered Tabela Inteira


#Definição de Produtos
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)


#Grafico de barras de Datas por Cidades
fig_date = px.bar(df_filtered, x="Date" , y="Total" , color="City" , title="Faturamento Por Dia:")
col1.plotly_chart(fig_date)


#Grafico de barras horizontais de Datas por Linha de Produtos
fig_product = px.bar(df_filtered, x="Date" , y="Product Line" , color="City" , title="Faturamento Por Tipo De Produto:" , orientation="h")
col2.plotly_chart(fig_product)


#Grafico de Barras grande de Faturamento Total Filial por CIdades
cidade_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_cidade = px.bar(df_filtered, x="City", y="Total" ,  title="Faturamento Por Filial:")
col3.plotly_chart(fig_cidade)


#Grafico de Barras grande de Faturamento de tipo de pagamento por Cidades
fig_pagamento = px.pie(df_filtered, values="Total", names="Payment" ,  title="Faturamento Por Tipo de Pagamento:")
col4.plotly_chart(fig_pagamento)