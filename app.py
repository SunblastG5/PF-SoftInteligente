import streamlit as st
from Fuzzy import ControlBrake
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

controlBrake = ControlBrake()

speed = st.slider(label="Seleccione la velocidad", min_value=0.0, max_value=100.0)
distance = st.slider(label="Seleccione la distancia", min_value=0.0, max_value=60.0)

if st.button("Aceptar"):
    controlBrake.setRules()
    st.write("Fuerza de freno")
    st.write(controlBrake.determine(speed,distance))





