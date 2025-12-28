import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Analizador Navideño", page_icon="🎅🏼")

# Título con estilo
st.title("🎅🏼 ¡Bienvenidos al analizador de conducta! 🤨")
st.markdown("### Vamos a ver si te portaste bien este año para recibir tu regalo 🎁")

# --- Sección de Datos Personales ---
st.subheader("Tus Datos 👤")
col1, col2 = st.columns(2)

with col1:
    nombre = st.text_input("¿Cómo te llamas?")
    edad = st.text_input("¿Cuántos años tienes?")

with col2:
    grado = st.text_input("¿A qué grado vas?")

st.divider() # Línea separadora

# --- Sección de Preguntas ---
st.subheader("Análisis de conducta 🔍")
st.write("Responde con sinceridad:")

preguntas = [
    "¿Te portaste muy bien con tu mamá y tu papá este año?",
    "¿Ordenaste tu habitación?",
    "¿Ayudaste con las tareas de la casa?",
    "¿Hiciste la tarea de la Escuela?",
    "¿Te lavaste los dientes todas las noches?",
    "¿Hablaste con respeto y sin decir malas palabras?",
    "¿Compartiste tus juguetes con otros niños?",
    "¿Fuiste amable con los animales?",
    "¿Fuiste amable con los demas?",
    "¿Comiste vegetales?"
]

# Creamos una lista para guardar las respuestas
respuestas = []

for i, p in enumerate(preguntas):
    # Usamos radio botones horizontales para que se vea más limpio
    opcion = st.radio(f"{i+1}. {p}", ["Sí ✅", "No ❌"], horizontal=True, key=f"p{i}")
    respuestas.append(opcion)

st.divider()

# --- Botón de Resultado ---
if st.button("🎁 ¡VER MI RESULTADO! 🎁"):
    if not nombre or not edad or not grado:
        st.warning("⚠️ ¡Espera! Santa necesita saber tu nombre, edad y grado.")
    else:
        # Contamos cuántos "Sí" hay
        puntos_si = respuestas.count("Sí ✅")
        
        if puntos_si >= 5: # Si tiene 5 o más respuestas positivas
            st.balloons() # ¡Efecto de globos en toda la pantalla!
            st.success(f"🎉🥳🎁 ¡Felicitaciones {nombre}!")
            st.write(f"A tus {edad} años, has demostrado ser una excelente persona en {grado}.")
            st.write("### ¡Te has portado muy bien y te mereces un gran regalo!")
        else:
            st.error(f"🤨 ¿Qué pasó, {nombre}?")
            st.write("Parece que hay algunas cositas que mejorar para el próximo año.")

            st.write("### Igual te toca un regalito pequeño. 🤏🏼")
