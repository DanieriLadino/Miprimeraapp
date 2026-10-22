import base64
import streamlit as st

# ---------- Perrito dibujado en el propio código (no necesita ningún archivo) ----------
PERRITO_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 420" width="320">
  <!-- cuerpo -->
  <ellipse cx="200" cy="335" rx="85" ry="70" fill="#D9C39A" stroke="#2B2B2B" stroke-width="6"/>
  <ellipse cx="200" cy="345" rx="30" ry="38" fill="#F3E8D2"/>
  <!-- patitas -->
  <ellipse cx="160" cy="395" rx="32" ry="20" fill="#D9C39A" stroke="#2B2B2B" stroke-width="6"/>
  <ellipse cx="240" cy="395" rx="32" ry="20" fill="#D9C39A" stroke="#2B2B2B" stroke-width="6"/>
  <!-- orejas -->
  <path d="M95 110 C40 110 20 190 55 230 C80 255 115 220 120 180 Z" fill="#D9C39A" stroke="#2B2B2B" stroke-width="6"/>
  <path d="M305 110 C360 110 380 190 345 230 C320 255 285 220 280 180 Z" fill="#D9C39A" stroke="#2B2B2B" stroke-width="6"/>
  <!-- cabeza -->
  <ellipse cx="200" cy="170" rx="115" ry="105" fill="#D9C39A" stroke="#2B2B2B" stroke-width="6"/>
  <!-- collar -->
  <path d="M135 262 Q200 290 265 262" fill="none" stroke="#E0A84A" stroke-width="14" stroke-linecap="round"/>
  <rect x="190" y="270" width="20" height="16" rx="3" fill="#C98E35" stroke="#2B2B2B" stroke-width="3"/>
  <!-- cejas -->
  <path d="M140 105 Q152 95 165 102" fill="none" stroke="#2B2B2B" stroke-width="5" stroke-linecap="round"/>
  <path d="M235 102 Q248 95 260 105" fill="none" stroke="#2B2B2B" stroke-width="5" stroke-linecap="round"/>
  <!-- ojos -->
  <circle cx="155" cy="150" r="27" fill="#FFFFFF" stroke="#2B2B2B" stroke-width="4"/>
  <circle cx="245" cy="150" r="27" fill="#FFFFFF" stroke="#2B2B2B" stroke-width="4"/>
  <circle cx="158" cy="153" r="20" fill="#1E1E1E"/>
  <circle cx="242" cy="153" r="20" fill="#1E1E1E"/>
  <circle cx="151" cy="145" r="7" fill="#FFFFFF"/>
  <circle cx="235" cy="145" r="7" fill="#FFFFFF"/>
  <circle cx="165" cy="160" r="3" fill="#FFFFFF"/>
  <circle cx="249" cy="160" r="3" fill="#FFFFFF"/>
  <!-- nariz -->
  <ellipse cx="200" cy="185" rx="20" ry="14" fill="#1E1E1E"/>
  <ellipse cx="194" cy="180" rx="6" ry="3" fill="#FFFFFF" opacity="0.8"/>
  <!-- boca y lengua -->
  <path d="M165 205 Q200 270 235 205 Q200 222 165 205 Z" fill="#3A2A22" stroke="#2B2B2B" stroke-width="4"/>
  <path d="M185 228 Q182 262 205 262 Q225 262 222 232 Q205 222 185 228 Z" fill="#E77B7B" stroke="#2B2B2B" stroke-width="4"/>
  <path d="M204 232 L204 252" stroke="#C85C5C" stroke-width="3" stroke-linecap="round"/>
</svg>
"""

def mostrar_perrito():
    b64 = base64.b64encode(PERRITO_SVG.encode("utf-8")).decode("utf-8")
    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="data:image/svg+xml;base64,{b64}" width="320"/>
            <p style="color:gray;">Perrito</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
# ----------------------------------------------------------------------------------------

st.title(" Mi Primera App!!")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
mostrar_perrito()


texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
       st.write('Correcto!')

with col2:
    st.subheader("Esta es la segunda columna")
    modo = st.radio("Que Modalidad es la principal en tu interfaz", ('Visual', 'auditiva', 'Táctil'))
    if modo == 'Visual':
       st.write('La vista es fundamental para tu interfaz')
    if modo == 'auditiva':
       st.write('La audición es fundamental para tu interfaz')
    if modo == 'Táctil':
       st.write('El tacto es fundamental para tu interfaz')

st.subheader("Uso de Botones")
if st.button('Presiona el botón'):
    st.write('Gracias por presionar')
else:
    st.write('No has presionado aún')

st.subheader("Selectbox")
in_mod = st.selectbox(
    "Selecciona la modalidad",
    ("Audio", "Visual", "Háptico"),
)
if in_mod == "Audio":
    set_mod = "Reproducir audio"
elif in_mod == "Visual":
    set_mod = "Reproducir video"
elif in_mod == "Háptico":
    set_mod = "Activar vibración"
st.write(" La acción es:" , set_mod)


with st.sidebar:
    st.subheader("Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva","Háptica")
    )
