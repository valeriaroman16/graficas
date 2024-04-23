#importamos la biblioteca streamlit
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#creamos el título de la app
st.title("Mi primera App")
st.header("Demo Titanic App")
st.write("Graficas del dataset")

titanic_link = 'titanic.csv'
titanic_data =pd.read_csv(titanic_link)
st.dataframe(titanic_data)

fig, ax = plt.subplots()
ax.hist(titanic_data["Fare"])
st.header("Histograma del Titanic")
st.pyplot(fig)

st.markdown("___")


fig2, ax2 = plt.subplots()
y_pos = titanic_data['Pclass']
x_pos = titanic_data['Fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Class")
ax2.set_xlabel("Fare")
ax2.set_title('¿Cuanto pagaron las clases del Titanic')
st.header("Grafica de Barras del Titanic")
st.pyplot(fig2)



st.markdown("___")


fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data.Age, titanic_data.Fare)
ax3.set_xlabel("Age")
ax3.set_ylabel("Fare")
st.header("Grafica de Dispersión del Titanic")
st.pyplot(fig3)

fig4, ax4 = plt.subplots()
ax4 = titanic_data.boxplot(["Age"])
ax4.set_ylabel("Tarifa")
st.header("Grafica de cajas por Edad")
st.pyplot(fig4)

fig5, ax5 = plt.subplots()
hist_class = np.histogram(titanic_data["Pclass"], bins=3, range=(1,3))[0]


labels = ['1', '2', '3']
colors = ['tab:blue', 'tab:red', 'tab:green']
explode = [0, 0, 0.2]


ax5.pie(hist_class,
       labels = labels,
         colors = colors,
         autopct='%.0f%%',
         explode = explode,
         shadow = True)
st.header("Grafica de pastel - Clase social")
st.pyplot(fig5)
st.dataframe(hist_class)
