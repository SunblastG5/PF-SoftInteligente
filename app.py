import streamlit as st
from Fuzzy import ControlBrake
from PIL import Image
from streamlit.components.v1 import html

image = Image.open('images/image.png')
st.sidebar.title("Proyecto Final - Software Inteligente")
with st.sidebar.expander("Información", True):
    st.markdown("""
        # Control de frenos.
        ## Curso  
        **Software Inteligente**
        ## Profesor: 
        **Calderón Vilca, Hugo David**
        ## Escuela Profesional:  
        **Ingeniería de Software** 
        ## Grupo 1
        * **Aguilar Salazar, Edwin Ccari**
        * **Alberto Miranda, Anderson Leandro**
        * **Arias Quispe, Alexis Enrique** 
        * **Bojorquez Suarez, Rafael Alejandro**
        * **Ramos Paredes, Roger Anthony**
    """)

st.title("Sistema de control de frenos usando Logica difusa")
controlBrake = ControlBrake()
controlBrake.setRules()

body="""<style>
        div.css-1v0mbdj.etr89bj1 {
            margin-left: 10%;
        }
        </style>
    """
st.markdown(body, unsafe_allow_html=True)

st.image(image)

speed = st.slider(label="Seleccione la velocidad", min_value=0.0, max_value=100.0)
distance = st.slider(label="Seleccione la distancia", min_value=0.0, max_value=60.0)

if st.button("Aceptar"):
    st.write("Fuerza de freno")
    st.write(f'{controlBrake.determine(speed,distance)} N')


