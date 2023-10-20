import streamlit as st
from api_utils import get_all_bikes, add_new_bike, update_bike  # Supondo que as funções estejam no arquivo 'your_api_module.py'

st.header("Cadastro de Bicicletas")

with st.expander("Ver todas as bicicletas"):
    success, all_bikes = get_all_bikes()
    col1, col2 = st.columns([4, 1])  # Criando duas colunas. A primeira é 4 vezes maior que a segunda.
    
    with col1:
        if success:
            st.empty()  # Limpando a coluna para não mostrar o resultado da requisição duas vezes.    
            st.write(all_bikes)
        else:
            st.write("Erro ao carregar as bicicletas.")
    with col2:
        if st.button("Atualizar"):
            success, all_bikes = get_all_bikes()
            if success:
                col1.empty()  # Limpando a coluna para não mostrar o resultado da requisição duas vezes.    
                col1.write(all_bikes)
            else:
                col1.write("Erro ao carregar as bicicletas.")

bike_id = st.text_input("ID da Bicicleta (Deixe em branco para nova bicicleta):")

marca = st.text_input("Marca:")
modelo = st.text_input("Modelo:")
cidade = st.text_input("Cidade:")

if bike_id:
    if st.button("Atualizar Bicicleta"):
        data = {"marca": marca, "modelo": modelo, "cidade": cidade}
        success, response = update_bike(bike_id, data)
        if success:
            st.success(f"Bicicleta {bike_id} atualizada com sucesso!")
        else:
            st.error(response["message"])
else:
    if st.button("Adicionar Nova Bicicleta"):
        data = {"marca": marca, "modelo": modelo, "cidade": cidade}
        success, response = add_new_bike(data)
        if success:
            st.success("Bicicleta adicionada com sucesso!")
        else:
            st.error(response["message"])
