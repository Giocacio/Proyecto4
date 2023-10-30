import pandas as pd 
import streamlit as st 
import plotly_express as px

st.header('Desarrollo Proyecto 4 (Datos anuncios venta de coches)')

data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
dis_button = st.button('Construir gráfico dispersión') # crear un botón
if dis_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.scatter(data, x="odometer", y="price")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)