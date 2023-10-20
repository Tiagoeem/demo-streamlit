import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.header("Análise")
st.write("Gráficos com Plotly aqui...")


tab1, tab2, tab3, tab4 = st.tabs(["Tabela", "Tabela Editavel", "Gráfico do Plotly", "Bubble Map"])

with tab1:
    st.header("Tabela")
    # Estudem como fazer cache: https://docs.streamlit.io/library/advanced-features/caching 
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')
    
    st.dataframe(df, use_container_width=True)

with tab2:

    st.header("Tabela Editavel")
    # Estudem como fazer cache: https://docs.streamlit.io/library/advanced-features/caching
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

    edited_df = st.data_editor(df)

with tab3:
    st.header("Gráfico do Plotly")

    df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
    fig = px.bar(df, y='pop', x='country', text_auto='.2s',
                title="Default: various text sizes, positions and angles")

    st.plotly_chart(fig, use_container_width=True)
    
with tab4:
                    
    st.header("Bubble Map - Plotly")

    df = px.data.gapminder().query("year==2007")
    fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
                        hover_name="country", size="pop",
                        projection="natural earth")

    st.plotly_chart(fig, use_container_width=True)