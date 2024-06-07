import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from resolucion import region_factible, graphical_method

st.title("Hola, bienvenid@ a la resolución de problemas por el :blue[Método Gráfico]")
if not "cuenta" in st.session_state:
    st.session_state.cuenta = 0


st.write("<h4> Primero ingresa tu funcion objetivo: </h4>", unsafe_allow_html= True)
cuenta = st.session_state.cuenta
columns = st.columns([0.1,0.3,0.1,0.3,0.3,0.1])

columns[0].text("")
columns[0].text("")
columns[0].write("Z =")
x1 = columns[1].number_input("", key="x1")
columns[2].text("")
columns[2].text("")
columns[2].markdown("X<sub>1</sub>", unsafe_allow_html=True)
signo = columns[3].selectbox(
    '',
    ('+','-')
)
x2 = columns[4].number_input("", key="x2", min_value=0)
columns[5].text("")
columns[5].text("")
columns[5].markdown("X<sub>2</sub>", unsafe_allow_html=True)

if signo== "-":
    x2 = -x2

seleccion_optimización = st.selectbox("¿Quieres maximizar o minimizar tu función?", options = ["Maximizar", "Minimizar"])
st.write("<h4> <span style='color:#5DADE2'> Ahora agrega tus restricciones: </span> </h4>", unsafe_allow_html= True)


if not "n_restricciones" in st.session_state:
    st.session_state.n_restricciones = 0

nr = st.session_state.n_restricciones

def suma_rest():
    st.session_state.n_restricciones += 1

columns = st.columns(2)
columns[1].button("Agregar restricción", on_click=suma_rest)



x1_rs = []
x2_rs = []
signo_rs =[]
signo_igualdad_rs = []
igualdad_rs = []

for i in range(nr):
    columns = st.columns([0.1,0.3,0.1,0.3,0.3,0.1,0.3,0.3])

    columns[0].text("")
    columns[0].text("")
    columns[0].write(f"R{i + 1}:")
    x1_r = columns[1].number_input("", key=f"x1_r{i}]")
    x1_rs.append(x1_r)
    columns[2].text("")
    columns[2].text("")
    columns[2].markdown("X<sub>1</sub>", unsafe_allow_html=True)
    signo_r1 = columns[3].selectbox(
        '',
        ('+','-'), key=f"s_r{i}"
    )
    signo_rs.append(signo_r1)
    x2_r = columns[4].number_input("", key=f"x2_r{i}", min_value=0)
    x2_rs.append(x2_r)
    columns[5].text("")
    columns[5].text("")
    columns[5].markdown("X<sub>2</sub>", unsafe_allow_html=True)  
    sig_igualdad_r = columns[6].selectbox(
        '',
        ('≤','≥','='), key=f"ig_r{i}"
    )
    signo_igualdad_rs.append(sig_igualdad_r)
    ig_r = columns[7].number_input("", key=f"ig_num_r{i}")
    igualdad_rs.append(ig_r)


columns = st.columns(2)


def resolucion():
    st.write("<h4> Ahora vamos a resolver el problema:  </h4>", unsafe_allow_html=True)
    coeficientes = []
    for i in range(nr):
        coef = np.array([x1_rs[i],x2_rs[i]])
        coeficientes.append(coef)
    coeficientes = np.array(coeficientes)
    bs = np.array(igualdad_rs)
    vertices, fig = region_factible(coefficients=coeficientes, bounds=bs, signs=signo_igualdad_rs)
    st.pyplot(fig)
    resultado_min, resultado_max = graphical_method(x1, x2, vertices)

    max_x1, max_x2, maxi = resultado_max
    min_x1, min_x2, mini = resultado_min


    if seleccion_optimización == "Minimizar":
        st.write("La solución para el mínimo es:", mini)
        st.write("Con x1 =", min_x1)
        st.write("Con x2 =", min_x2)
        return min_x1, min_x2, mini

    if seleccion_optimización == "Maximizar":
        st.write("La solución para el máximo es:", maxi)
        st.write("Con x1 =", max_x1)
        st.write("Con x2 =", max_x2)
        return max_x1, max_x2, maxi


if st.session_state.n_restricciones:
    listo = columns[1].button("Listo")

    if listo:
        st.markdown(f"""<p style='text-align: center;'>Tu función objetivo es    
                    <span style='color:#7FCBCE'><b>Z</b> = {x1} <b>X<sub>1</sub></b> {signo} 
                    {abs(x2)}<b>X<sub>2</sub></b></span></p>""", unsafe_allow_html=True,)
        for i in range(nr):
            st.markdown(f"""<p style='text-align: center;'>Tus restricciones son :    
                        <span style='color:#7FCBCE'><b>R{i + 1} </b> = {x1_rs[i]} <b>X<sub>1</sub></b> {signo_rs[i]} 
                        {x2_rs[i]} <b>X<sub>2</sub></b> {signo_igualdad_rs[i]} {igualdad_rs[i]} </span></p>  """, unsafe_allow_html=True,)
            
        v1, v2, r = resolucion()

        if st.session_state.n_restricciones == 2:
            st.title("Análisis de sensibilidad")
            s1 = r / x1
            s2 = r / x2

            m_tmp = -s2 / s1

            x_tmp = np.linspace(-0.1, s1 + 0.1, 1000)
            y_tmp = m_tmp * x_tmp + s2

            fig, ax = plt.subplots()
            ax.plot(x_tmp, y_tmp)
            ax.plot(np.linspace(0, s1 + 1, 2), np.zeros(2), '--', c = 'black')
            ax.plot(np.zeros(2), np.linspace(0, s2 + 1, 2), '--', c = 'black')
            ax.scatter(v1, v2, c='r', label = "FEV")
            ax.text(v1 + 0.1, v2 + 0.1, f"({v1}, {v2})")
            ax.legend()
            
            st.pyplot(fig)

            st.title("Intervalo de optimalidad")

            c1_x1, c1_x2 = x1_rs
            c2_x1, c2_x2 = x2_rs

            div1 = c1_x1 / c2_x1
            div2 = c1_x2 / c2_x2
            
            ma, mi = max(div1, div2), min(div1, div2)
            st.write(f"{mi:.2f}" + r" ≤ $\frac{c_1}{c_2}$ ≤ " + f"{ma:.2f}")

            new_1, new_2 = div1 * x2, div2 * x2
            ma, mi = max(new_1, new_2), min(new_1, new_2)

            st.write(f"{mi:.2f}" + r" ≤ $c_1$ ≤ " + f"{ma:.2f}")

            new_1, new_2 = div1 ** -1 * x1, div2 ** -1 * x1
            ma, mi = max(new_1, new_2), min(new_1, new_2)

            st.write(f"{mi:.2f}" + r" ≤ $c_2$ ≤ " + f"{ma:.2f}")


