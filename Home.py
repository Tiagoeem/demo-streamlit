import streamlit as st
import requests


st.header("Olá Streamlit!")

# Configuração
#st.set_page_config(layout="wide")

# Definindo as tabs
tab1, tab2 = st.tabs(["Requisição", "Imagem"])

with tab1:
    st.header("Faça uma requisição GET")

    # Criando as colunas para a URL e para a resposta
    col1, col2 = st.columns([2, 2])

    # Coluna da URL
    with col1:
        url = st.text_input("Digite a URL:")
        if st.button("Enviar Requisição"):
            try:
                response = requests.get(url)
                response.raise_for_status()  # Levanta uma exceção se a resposta não for 200 OK
                st.session_state.response_text = response.text
            except requests.RequestException as e:
                st.session_state.response_text = f"Erro ao fazer a requisição: {e}"

    # Coluna da Resposta
    with col2:
        if "response_text" in st.session_state:
            st.text_area("Resposta:", value=st.session_state.response_text, height=250)

with tab2:
    st.header("Um gato fofo")
    st.image("https://pub-213de2be34304c7991f0aa38af54f15e.r2.dev/Um gato fofo.jpeg", width=300)
    st.balloons()