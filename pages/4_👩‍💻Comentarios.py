import streamlit as st
st.title(":blue[Deja un comentario!]")
# Carga de la imagen
st.image("robotintro-dribble-unscreen (1).gif")

# Caja de comentarios
comment = st.text_area("Nos ayudaria mucho saber que opinas de la página, asi que te invitamos a dejar algun comentario o sugerencia, gracias !!!")

# Botón para enviar el comentario
if st.button("Enviar"):
    if comment:
        # Guardar el comentario en un archivo de texto
        with open("comentarios.txt", "a") as f:
            f.write(comment + "\n")
        
        st.success("Gracias por tu comentario!")
        st.write("Comentario enviado:")
        st.write(comment)
    else:
        st.error("Por favor, escribe un comentario antes de enviar.")
