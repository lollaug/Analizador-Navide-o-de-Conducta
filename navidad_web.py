
import streamlit as st

# --- Configuración de la página (¡Importante para el título de la pestaña del navegador!) ---
st.set_page_config(page_title="🎄 Analizador de Conducta Navideño 🎅🏼", page_icon="🎁")

# --- MENSAJE DE BIENVENIDA ESPECIAL CON IMAGEN ---
# Cambia el 300 por el número que prefieras (más pequeño = menos píxeles)
# Creamos 3 columnas. Los números [1, 2, 1] definen el ancho proporcional.
# La columna del medio (2) es el doble de ancha que las de los lados (1).
col_izq, col_centro, col_der = st.columns([1, 2, 1])

with col_centro:
    # Aquí la imagen se adapta al ancho de la columna central
    st.image("https://i.pinimg.com/736x/47/7a/83/477a8332d91122c2ab1c69306687151c.jpg", use_container_width=True)
st.markdown(
    """
    <div style="text-align: center; background-color: #fce4ec; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
        <h1 style="color: #d32f2f; font-family: 'Helvetica', bold;">
            🎅🏼 ¡Bienvenidos al Analizador de Conducta de Navidad! 🤨
        </h1>
        <p style="color: #424242; font-size: 1.0em;">
            Vamos a ver si te portaste bien este año, para recibir tu regalo 🎁. <br>
            ¡Responde con honestidad!
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.divider() # Una línea decorativa para separar

# --- Sección de Datos Personales ---
st.subheader("📝 Cuéntanos sobre ti:")
col1, col2 = st.columns(2) # Divide la pantalla en dos columnas

with col1:
    nombre = st.text_input("¿Cuál es tu nombre? 👤")
    edad = st.text_input("¿Cuántos años tienes? 🎂")

with col2:
    grado = st.text_input("¿A qué grado de la escuela vas? 📚")

st.divider()

# --- Sección de Preguntas ---
st.subheader("👀 Hora de revisar tu año:")
st.write("¡Responde **'Sí'** o **'No'** a cada pregunta para ayudar a Santa!")

preguntas = [
    "¿Te portaste muy bien con tu mamá y tu papá este año?",
    "¿Ordenaste tu habitación sin que te lo dijeran?",
    "¿Ayudaste con las tareas de la casa cuando te lo pidieron?",
    "¿Hiciste la tarea de la Escuela siempre a tiempo?",
    "¿Te lavaste los dientes todas las noches sin que te recordaran?",
    "¿Hablaste con respeto y sin decir malas palabras a nadie?",
    "¿Compartiste tus juguetes con otros niños o hermanos?",
    "¿Fuiste amable y cuidadoso con los animales?",
    "¿Fuiste amable con los demas?",
    "¿Comiste frutas y verduras?"
]

# Creamos una lista para guardar las respuestas de los botones de radio
respuestas_radio = []

for i, p in enumerate(preguntas):
    # Usamos st.radio para cada pregunta, con opciones Sí/No
    # La clave 'key' es importante para que Streamlit sepa qué botón es cuál
    opcion = st.radio(f"{i+1}. {p}", ["Sí ✅", "No ❌"], horizontal=True, key=f"pregunta_{i}")
    respuestas_radio.append(opcion)

st.divider()

# --- Botón para analizar la conducta ---
if st.button("✨ ¡VERIFICAR MI CONDUCTA! ✨", use_container_width=True, type="primary"):
    # Validar que los datos personales estén completos
    if not nombre.strip() or not edad.strip() or not grado.strip(): # .strip() para ignorar espacios en blanco
        st.warning("⚠️ ¡Ups! Santa necesita todos tus datos (nombre, edad, grado) para revisar tu lista.")
    else:
        puntos_positivos = respuestas_radio.count("Sí ✅")
        total_preguntas = len(preguntas)
        
        # Calcular el porcentaje de respuestas positivas
        porcentaje_positivo = (puntos_positivos / total_preguntas) * 100

        st.subheader("🎉 ¡RESULTADO FINAL DE SANTA! 🎉")

        # Lógica de decisión: Más del 60% de "Sí" para el regalo grande
        if porcentaje_positivo >= 60: 
            st.balloons() # ¡Efecto de globos en la pantalla!
            st.success(f"¡Felicitaciones {nombre}, **¡Estás en la Lista de Buenos!**")
            st.write(f"Con {puntos_positivos} respuestas positivas, a tus {edad} años y en {grado}, ¡te mereces un **GRAN REGALO** esta Navidad! 🎁✨")
            st.snow() # Efecto de nieve
        else:
            st.error(f"¡Oh!, ¿Qué pasó {nombre}? **¡Parece que hay algunas cositas que mejorar!**")
            st.write(f"Con {puntos_positivos} respuestas positivas, aún puedes pulir tu conducta.")
            st.write("Pero no te preocupes, ¡Santa es generoso! Igual te espera un **regalito pequeño** para que te animes a portarte aún mejor el próximo año. 🤏🏼🎄")





