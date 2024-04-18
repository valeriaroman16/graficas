#importamos la biblioteca streamlit
import pandas as pd
import streamlit as st

#creamos el título de la app
st.title("Mi primera App")
st.header("Demo Titanic App")
st.write("Graficas del dataset")

titanic_link = 'titanic.csv'
titanic_data =pd.read_csv(titanic_link)
st.dataframe(titanic_data)