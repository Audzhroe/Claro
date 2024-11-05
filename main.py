import streamlit as st


st.title('Mi primerra aplicación de Streamlit')

st.header('!Hola, Streamlit!')
st.write('Esto es una aplicación simple')
st.image('logo.png')
if st.button('Presiona Aqui',key = 1)

input = st.text_input('Escribe algo',key = 2)
st.write('Escribiste:', input)

st.sidebar.title('Mi Primera barra lateral de Streamlit')
st.sidebar.header('!Hola, Barra Lateral!')
st.sidebar.write('Esto es una barra lateral')
st.sidebar.image('logo.png')

if st.sidebar.button('Presiona Aqui',key = 4):
    st.sidebar.write('Has presionado el botón')


input = st.sidebar.text_input('Escribe algo',key = 3)
st.sidebar.write('Escribiste:', input)
