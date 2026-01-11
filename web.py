import streamlit as st
import os

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Los Vasos de Luli | Repostería", layout="wide")

# Ocultar menús de Streamlit para acabado profesional
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0px !important;}
        iframe {border: none !important;}
    </style>
""", unsafe_allow_html=True)

# 2. DATOS DE LA EMPRESA
INFO = {
    "nombre": "Los Vasos de Luli",
    "ubicacion": "Repostería Artesanal",
    "descripcion": "Transformamos ingredientes seleccionados en obras de arte comestibles. Especialistas en repostería fina de autor para momentos inolvidables.",
    "whatsapp": "51977905037",
    "instagram": "https://www.instagram.com/losvasosdeluli7/",
    "facebook": "https://www.facebook.com/profile.php?id=61568275415704",
    "tiktok": "https://www.tiktok.com/@losvasitosdeluli7?fbclid=IwY2xjawPQnldleHRuA2FlbQIxMABicmlkETFPd3ZFM2JNN3dHSTZZWjBQc3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHm5uUqWN0jxBygcGWxXuy6aLmcVpomJr89tDItB2lp-9EK8Iby1DOUij_7Zh_aem_PxVxW-BI4eFRJ0Q-Qpq-rQ"
}

# 3. FUNCIÓN PARA CARGAR EL HTML
def cargar_diseño(ruta):
    if os.path.exists(ruta):
        with open(ruta, 'r', encoding='utf-8') as f:
            html = f.read()
            # Reemplazo de variables manual (estilo Flask)
            for clave, valor in INFO.items():
                html = html.replace(f"{{{{ {clave} }}}}", str(valor))
            return html
    return "<h1>Error: No se encontró el archivo index.html</h1>"

# 4. RENDERIZAR
diseño_final = cargar_diseño("index.html")
st.components.v1.html(diseño_final, height=2000, scrolling=False)
