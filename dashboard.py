import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Análise de dados")

arquivo_upload = st.file_uploader("Escolha o arquivo CSV", type = "csv")  #Upload de arquivos

if arquivo_upload is not None:
    df = pd.read_csv(arquivo_upload)
    st.subheader("Visualização dos dados")
    st.write(df.head())

    st.subheader("Resumo dos dados")
    colunas = df.columns.tolist()
    st.write(df.style.highlight_max(axis=0, subset=df.drop(columns = ['Data','Cidade']).columns))
    st.markdown(''':orange[As caixas selecionadas em amarelo representam os maiores resultados para cada tipo de dado]''')


    st.subheader("Filtragem de dados")
    colunas_selecionadas = st.selectbox("Selecione a coluna a ser filtrada", colunas)
    valores_unicos = df[colunas_selecionadas].unique()
    valores_selecionados = st.selectbox("Selecione o valor", valores_unicos)

    df_filtrado = df[df[colunas_selecionadas] == valores_selecionados]
    st.write(df_filtrado)

    st.subheader("Dados do gráfico")
    x_coluna = st.selectbox("Selecione os dados do eixo x", colunas)
    
    if x_coluna == "Cidade":
        cidades = df["Cidade"].unique()
        cidade_selecionada = st.selectbox("Selecione a cidade", cidades)
        df_filtrado = df[df["Cidade"] == cidade_selecionada]  

    y_coluna = st.selectbox("Selecione os dados do eixo y", colunas)

    if st.button("Criar gráfico"):
        try:
            st.line_chart(df_filtrado.set_index(x_coluna)[y_coluna])
            
        except KeyError:
            st.error("Erro ao gerar o gráfico. Certifique-se de que os eixos estão corretos.")
    else:
        st.write("Esperando o envio dos dados...")

 