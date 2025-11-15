import streamlit as st
from pymongo import MongoClient
import pandas as pd

# Conectando ao MongoDB
client = MongoClient('mongodb://mongo:27017/')
db = client['eshop']
collection = db['clientes']

# Streamlit
st.title("Gestão de Dados - E-Shop Brasil")

menu = st.sidebar.selectbox("Menu", ["Inserir Dados", "Visualizar Dados", "Editar/Excluir"])

if menu == "Inserir Dados":
    nome = st.text_input("Nome:")
    email = st.text_input("Email:")
    if st.button("Salvar"):
        collection.insert_one({"nome": nome, "email": email})
        st.success("Cliente adicionado!")

elif menu == "Visualizar Dados":
    dados = list(collection.find())
    df = pd.DataFrame(dados)
    st.dataframe(df)

elif menu == "Editar/Excluir":
    dados = list(collection.find())
    df = pd.DataFrame(dados)
    st.dataframe(df)
    st.write("Selecione pelo ID para editar ou excluir.")
