import streamlit as st

def saludar(nombre):
    return f"Hola {nombre}, ¡saludando desde Streamlit en Render!"

def calcular_cuadrado(numero):
    return f"El cuadrado de {numero} es: {numero ** 2}"

st.title("Aplicación de Streamlit en Render")

# Saludo
st.subheader("Saludo interactivo")
nombre = st.text_input("Tu nombre")
if st.button("Saludar"):
    st.write(saludar(nombre))

st.divider()

# Cálculo
st.subheader("Cálculo numérico")
numero = st.slider("Elegí un número", 1, 10, 1)
if st.button("Calcular cuadrado"):
    st.write(calcular_cuadrado(numero))