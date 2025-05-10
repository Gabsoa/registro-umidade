import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Nome do arquivo Excel
ARQUIVO = "teste_registro.xlsx"

# Função para carregar os dados existentes ou criar novo DataFrame
def carregar_dados():
    if os.path.exists(ARQUIVO):
        return pd.read_excel(ARQUIVO)
    else:
        colunas = ["Turno", "Nome do operador", "Horário", "Umidade", "Temperatura", "Toneladas"]
        return pd.DataFrame(columns=colunas)

# Função para salvar os dados no Excel
def salvar_dados(df):
    df.to_excel(ARQUIVO, index=False)

# Carrega dados existentes
df_existente = carregar_dados()

# Título e layout
st.set_page_config(page_title="Registro de umidade -Teste-", layout="centered")
st.title("Registro de umidade -Teste-")
st.markdown("Preencha os campos abaixo para adicionar uma nova entrada:")

# Formulário para nova entrada
with st.form("formulario_dados", clear_on_submit=True):
    turno = st.selectbox("Turno", ["A1", "A2", "B1", "B2"])
    nome = st.text_input("Nome do operador")
    horario = st.text_input("Horário da amostra")
    umidade = st.number_input("Umidade (%)")
    temperatura = st.number_input("Temperatura (°C)")
    toneladas = st.number_input("Toneladas")
    
    submit = st.form_submit_button("Salvar")

    if submit:
        nova_linha = {
            "Turno": turno,
            "Nome do operador": nome,
            "Horário": horario,
            "Umidade": umidade,
            "Temperatura": temperatura,
            "Toneladas": toneladas,
            }
        
        df_novo = pd.DataFrame([nova_linha])
        df_atualizado = pd.concat([df_existente, df_novo], ignore_index=True)
        salvar_dados(df_atualizado)
        st.success("✅ Dados salvos com sucesso!")
        

# Visualização de dados existentes
with st.expander("📁 Visualizar dados existentes"):
    st.dataframe(df_existente)
