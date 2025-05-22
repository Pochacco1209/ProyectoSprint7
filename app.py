import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('C:/Users/marth/ProyectoSprint7/notebooks/vehicles_us.csv') # leer los datos
st.header('Aplicación Web de un Sitio de Autos')
#Crea un boton en la pag. web
hist_boton = st.button('Construir Histograma')
disp_boton = st.button('Construir Diagrama de Dispersión')
build_histogram = st.checkbox('Construir un Histrograma')
build_dispersion = st.checkbox('Construir un Diagrama de Dispersión')

if hist_boton: #indica "Si es precionado el botón entonces:..."
    #escribe un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    #crea el histograma
    fig = px.histogram(car_data, x='odometer')

    #muestra un gráfico de Plotly interactivo
    st.plotly_chart(fig, user_container_width=True)

if disp_boton:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, user_container_width=True)

if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, user_container_width=True)

if build_dispersion:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, user_container_width=True)

