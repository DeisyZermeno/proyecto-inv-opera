import streamlit as st
st.title(":blue[Analisis de Sensibilidad]")
st.markdown("""<p style='font-size: 20px;'>El análisis de sensibilidad se realiza despues de obtener la solucion
          optima de un modelo lineal para deteminar como afectan los cambios en los parametros del
        modelo a la solución óptima calculada.</p>""", unsafe_allow_html=True)
st.write("Veamos con un ejemplo como funciona :")

st.write("Este programa resuelve un problema de programación lineal utilizando el método de la función objetivo y restricciones proporcionadas.")

# Introducción del problema
st.subheader("Descripción del Problema")
st.write("""Un agricultor está planeando cultivar dos tipos de cultivos en su granja: maíz y frijoles. El maíz tiene un rendimiento de \$30 pesos por hectárea y los frijoles tienen
          un rendimiento de \$20 por hectárea. El agricultor quiere maximizar sus ganancias, 
         representadas por la función objetivo Z = 30X<sub>1</sub> + 20X<sub>2</sub>, donde
          X<sub>1</sub>es la cantidad de 
         hectáreas plantadas con maíz y X<sub>2</sub> es la cantidad de hectáreas plantadas con frijoles
         .""", unsafe_allow_html=True)
st.write("Sin embargo, hay algunas restricciones que debe tener en cuenta:")

# Restricciones
st.subheader("Restricciones")
st.write("1. El agricultor solo tiene disponible un máximo de 8 horas de riego por semana: 2X<sub>1</sub>+ X<sub>2</sub>  ≤ 8", unsafe_allow_html= True)
st.write("2. Además, la mano de obra disponible es limitada, con un máximo de 8 horas de trabajo por semana: X<sub>1</sub> + 3X<sub>2</sub>  ≤ 8", unsafe_allow_html= True )


st.write("Tenemos una función objetivo a maximizar :")
st.markdown("<p style='font-size: 25px; color: lightblue;'>Z = 30 X<sub>1</sub> + 20 X<sub>2</sub></p>", unsafe_allow_html=True)
st.write("Con restricciones:")

st.markdown("<p style='font-size: 25px; color: darkseagreen;'>R<sub>1</sub> = 2 X<sub>1</sub> + 1 X<sub>2</sub>  ≤ <span style='color:#c55951'>8</span>  </p>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 25px; color: darkseagreen;'>R<sub>2</sub> = 1 X<sub>1</sub> + 3 X<sub>2</sub>  ≤ <span style='color:#c55951'>8</span> </p>", unsafe_allow_html=True)
st.write("Al realizar el analisis por el método grafico podemos veer que obtenemos una solución optima en los puntos:")


# Divide el espacio en dos columnas
col1, col2, col3 = st.columns(3)

#  texto en la primera columna
with col1:
    st.markdown("<p style='font-size: 25px; color: darkseagreen;'>X<sub>1</sub> = 10/5</p>", unsafe_allow_html=True)

# Escribe el segundo texto en la segunda columna
with col2:
    st.markdown("<p style='font-size: 25px; color: darkseagreen;'>X<sub>2</sub> = 8/5</p>", unsafe_allow_html=True)
with col3:
    st.markdown("<p style='font-size: 25px; color: darkseagreen;'>Z = 128</p>", unsafe_allow_html=True)

st.markdown("""<p style='font-size: 20px;'><span style='color:#7FCBCE'>Intervalo Variación Coeficiente Función Objetivo.</span></p>""", unsafe_allow_html=True)

st.write("Ahora el valor de <span style='color:#7FCBCE'>Z</span> lo denotamos como <span style='color:#9EA4E8'>Z*</span>", unsafe_allow_html=True)

st.write("Ahora podemos graficare la <span style='color:#9EA4E8'>Z*</span> dentro del plano de las variables no básicas.", unsafe_allow_html=True)
st.write("Con la nueva funcion objetivo:")

st.markdown("""
<p style='font-size: 20px;'>
    <span style='color: #9EA4E8;'>Z*</span> = 30 
    <span style='color: #9EA4E8;'>X<sub>1</sub></span> + 20 
    <span style='color: #9EA4E8;'>X<sub>2</sub></span> = 128
</p>
""", unsafe_allow_html=True)
st.write("Para X<sub>2</sub> =0: ",unsafe_allow_html=True) 
st.write(" <span style='color:#9EA4E8'>X<sub>1</sub></span>  = 128/30 =  <span style='color:#9EA4E8'>4.26</span>", unsafe_allow_html=True)
st.write(" <span style='color:#9EA4E8'>X<sub>1</sub></span>  = 128/30 =  <span style='color:#9EA4E8'>4.26</span>", unsafe_allow_html=True)

st.write("Para X<sub>1</sub> =0: ",unsafe_allow_html=True) 
st.write(" <span style='color:#9EA4E8'>X<sub>1</sub></span>  = 128/30 =  <span style='color:#9EA4E8'>4.26</span>", unsafe_allow_html=True)
st.write(" <span style='color:#9EA4E8'>X<sub>2</sub></span>  = 128/20 =  <span style='color:#9EA4E8'>6.4</span>", unsafe_allow_html=True)

st.write("Entonces gráficamente tendremos: GRAFICOOOOOO")

st.write("""De manera que los coeficientes de <span style='color:#7FCBCE'>Z = C<sub>1</sub>X<sub>1</sub> + 
         C<sub>2</sub>X<sub>2</sub></span> pueden variar siempre y cuando se encuentren dentro del 
         intervalo de optimalidad.""", unsafe_allow_html=True)

st.write("La pendiente entre los valores de las restricciones R<sub>1 </sub> y  R<sub>2 </sub> pueden ser:")

st.write("C<sub>1</sub>X<sub>1</sub> + C<sub>2</sub>X<sub>2</sub> =  <span style='color:#c55951'>8</span> ", unsafe_allow_html=True)
st.write("C<sub>1</sub>X<sub>1</sub> + C<sub>2</sub>X<sub>2</sub> =  <span style='color:#c55951'>8</span> ", unsafe_allow_html=True)

st.write("Sabemos que la pendiente de una recta viene dada por la expresión:")
st.latex(r'''
m = \frac{C_1}{C_2}
''')

st.write("""Para obtener el intervalo de optimalidad solo bastará con 
         dividir el coeficiente de la restricción 1 de la X<sub>1</sub> y
         el coeficiente de la restricción 2 para tambien la  X<sub>1</sub>  , 
         de la misma manera para X<sub>2</sub>. 
         <br/>En nuestro caso deberemos tomar para X<sub>1</sub>: """, unsafe_allow_html=True)


# Divide el espacio en dos columnas
col1, col2, col3 = st.columns(3)

#  texto en la primera columna
with col1:
    st.markdown("<p style='font-size: 18px; color: darkseagreen;'>   R<sub>1</sub> = <span style='color:#c55951'>2</span> X<sub>1</sub>  </p>", unsafe_allow_html=True)
with col2:
    st.markdown("<p style='font-size: 18px; color: darkseagreen;'>   R<sub>2</sub> = <span style='color:#c55951'>1</span> X<sub>1</sub>  </p>", unsafe_allow_html=True)
with col3:
    st.markdown(r'<span style="color:#c55951;">$$\frac{2}{1}$$</span>', unsafe_allow_html=True)
st.write("para X<sub>1</sub>",unsafe_allow_html=True)

# Divide el espacio en dos columnas
col1, col2, col3 = st.columns(3)

#  texto en la primera columna
with col1:
    st.markdown("<p style='font-size: 18px; color: darkseagreen;'>   R<sub>1</sub> = <span style='color:#c55951'>1</span> X<sub>2</sub>  </p>", unsafe_allow_html=True)
with col2:
    st.markdown("<p style='font-size: 18px; color: darkseagreen;'>   R<sub>2</sub> = <span style='color:#c55951'>3</span> X<sub>2</sub>  </p>", unsafe_allow_html=True)
with col3:
    st.markdown(r'<span style="color:#c55951;">$$\frac{1}{3}$$</span>', unsafe_allow_html=True)
st.write("Entonces tendremos :")




st.write("Tendremos entonces un intervalo de optimalidad de:")

st.markdown(r'''
<span style="color: #c55951; text-align: center; display: block;">$$\frac{1}{3} \leq \frac{C_1}{C_2} \leq 2$$</span>
''', unsafe_allow_html=True)

st.write("""Entonces tomando de nuestra función objetio los valores de
          C<sub>1</sub> = 30 y de C<sub>2</sub> = 20, podemos establecer un intervalo para 
         la solucion optima de modo que """, unsafe_allow_html=True)


st.markdown(r'''
<span style="color: #c55951; text-align: center; display: block;">$$\frac{1}{3} \leq \frac{C_1}{20} \leq 2$$</span>
''', unsafe_allow_html=True)

st.markdown(r'''
<span style="color: #c55951; text-align: center; display: block;">$$ 6.666 \leq C_1 \leq 40$$</span>
''', unsafe_allow_html=True)

st.write("En este caso la utilidad por hectárea del cultivo de maiz puede variar entre 6.666 hectareas y 40 hectareas ")
