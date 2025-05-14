import streamlit as st
import pandas as pd
import os
import openpyxl as op
from datetime import datetime

# Nome do arquivo Excel
ARQUIVO = "2. Planilha de UMIDADE.xlsx"

# Função para carregar os dados existentes ou criar novo DataFrame
def carregar_dados():
    if os.path.exists(ARQUIVO):
        return pd.read_excel(ARQUIVO)
    else:
        colunas = ["DATA","TURNO", "OPEDADOR", "HORÁRIO", "UMIDADE", "TEMPERATURA", "TONELADAS", "CONTROLE DE UMIDADE LIGADO", "POSIÇÃO DO ARADO"]
        return pd.DataFrame(columns=colunas)

# Função para salvar os dados no Excel
def salvar_dados(df):
    df.to_excel(ARQUIVO, index=False)

# Carrega dados existentes
df_existente = carregar_dados()

# Título e layout
st.set_page_config(page_title="Registro de umidade -Teste-", layout="centered")
st.title("Registro de umidade -Teste-")


# Formulário para nova entrada
with st.form("formulario_dados", clear_on_submit=True):
    DATA = st.text_input("Data")
    TURNO = st.selectbox("Turno", ["A1", "A2", "B1", "B2"])
    OPERADOR = st.text_input("Nome do operador")
    HORÁRIO = st.text_input("Horário da amostra")
    UMIDADE = st.number_input("Umidade (%)")
    TEMPERATURA = st.number_input("Temperatura (°C)")
    TONELADAS = st.number_input("Toneladas (T)")
    CONTROLE DE UMIDADE LIGADO = st.selectbox("Controle de umidade",["Sim", "Não"])
    POSIÇÃO DO ARADO = st.selectbox("Posição do arado", ["Elevado", "Abaixado"])
    
    submit = st.form_submit_button("Salvar")

    if submit:
        nova_linha = {
            "DATA": data,
            "TURNO": turno,
            "OPERADOR": nome do operador,
            "HORÁRIO": horario,
            "UMIDADE": umidade,
            "TEMPERATURA": temperatura,
            "TONELADAS": toneladas,
            "CONTROLE DE UMIDADE LIGADO": controle de umidade,
            "POSIÇÃO DO ARADO": posição do arado
            }
        
        df_novo = pd.DataFrame([nova_linha])
        df_atualizado = pd.concat([df_existente, df_novo], ignore_index=True)
        salvar_dados(df_atualizado)
        st.success("✅ Dados salvos com sucesso!")
        

# Visualização de dados existentes
with st.expander("📁 Visualizar dados existentes"):
    st.dataframe(df_existente)
