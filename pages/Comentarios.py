import streamlit as st
import numpy as np
from scipy.optimize import linprog
st.markdown(
    """
    <style>
    .main {
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("robotintro_dribble.gif")



# Agregar el estilo al markdown
st.markdown(style, unsafe_allow_html=True)

# Caja de comentarios
comment = st.text_area("Deja tu comentario aquí:")
if st.button("Enviar"):
    if comment:
        with open("comentarios.txt", "a") as f:
            f.write(comment + "\n")
        
        st.markdown("<span class='blue-text'>Gracias por tu comentario!</span>", unsafe_allow_html=True)
        st.markdown("<span class='blue-text'>Comentario enviado:</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='blue-text'>{comment}</span>", unsafe_allow_html=True)
    else:
        st.markdown("<span class='blue-text'>Por favor, escribe un comentario antes de enviar.</span>", unsafe_allow_html=True)
        