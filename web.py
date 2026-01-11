import streamlit as st
import streamlit.components.v1 as components
import os
from datetime import datetime

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Los Vasos de Luli | Repostería", layout="wide")

# Ocultar menús de Streamlit para que parezca una web profesional
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0px !important;}
    </style>
""", unsafe_allow_html=True)

# 2. TUS DATOS (Copiados de tu web.py)
INFO = {
    "nombre": "Los Vasos de Luli",
    "ubicacion": "Repostería Artesanal",
    "descripcion": "Transformamos ingredientes seleccionados en obras de arte comestibles. Especialistas en repostería fina de autor para momentos inolvidables.",
    "whatsapp": "51977905037",
    "instagram": "https://www.instagram.com/losvasosdeluli7/",
    "facebook": "https://www.facebook.com/profile.php?id=61568275415704"
}

SERVICIOS = [
    {"icono": "fa-birthday-cake", "nombre": "Tortas de Autor"},
    {"icono": "fa-ice-cream", "nombre": "Postres de Vitrina"},
    {"icono": "fa-box-open", "nombre": "Cajas de Regalo"},
    {"icono": "fa-cookie-bite", "nombre": "Petit Fours"},
    {"icono": "fa-gem", "nombre": "Ingredientes Premium"},
    {"icono": "fa-truck", "nombre": "Delivery Seguro"},
    {"icono": "fa-utensils", "nombre": "Catering para Eventos"},
    {"icono": "fa-heart", "nombre": "Opciones Sin Azúcar"},
    {"icono": "fa-certificate", "nombre": "Calidad Gourmet"},
]

TESTIMONIOS = [
    {"nombre": "Valeria S.", "comentario": "La choco fresa fue el centro de atención en mi boda. ¡Increíble!"},
    {"nombre": "Marco R.", "comentario": "El mejor pie de lúcuma que he probado en mi vida. La presentación es impecable."},
    {"nombre": "Empresa TechX", "comentario": "Nuestros clientes quedaron fascinados con las cajas de regalo personalizadas."}
]

# 3. LÓGICA DE GALERÍA
# En Streamlit Cloud, las imágenes deben estar en una carpeta dentro de tu repo de GitHub
# Para este ejemplo, usaremos placeholders si la carpeta no existe, 
# pero el código ya busca en 'static/img'
galeria_html = ""
mensaje_ws = f"Hola, vi la web de {INFO['nombre']} y quisiera el catálogo de postres."
ws_link = f"https://wa.me/{INFO['whatsapp']}?text={mensaje_ws.replace(' ', '%20')}"

# --- CONSTRUCCIÓN DEL HTML PRO ---
servicios_html = "".join([f"""
    <div class="col-md-4 col-6 mb-4">
        <div class="service-card p-4 bg-white rounded shadow-sm">
            <i class="fas {s['icono']} fa-2x mb-3" style="color: #c5a47e;"></i>
            <h6 class="text-uppercase small fw-bold">{s['nombre']}</h6>
        </div>
    </div>
""" for s in SERVICIOS])

testimonios_html = "".join([f"""
    <div class="col-md-4 mb-4">
        <div class="p-4 border border-secondary rounded-4">
            <p class="fst-italic opacity-75">"{t['comentario']}"</p>
            <small class="text-uppercase" style="color: #c5a47e;">{t['nombre']}</small>
        </div>
    </div>
""" for t in TESTIMONIOS])

# 4. EL CÓDIGO HTML/CSS COMPLETO
html_final = f"""
<!DOCTYPE html>
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Playfair+Display:wght@700&family=Great+Vibes&display=swap" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <style>
        :root {{ --gold: #c5a47e; --dark: #1a1a1a; }}
        body {{ font-family: 'Poppins', sans-serif; color: var(--dark); overflow-x: hidden; }}
        
        /* SPLASH SCREEN */
        .splash-screen {{
            position: fixed; top: 0; left: 0; width: 100%; height: 100vh;
            background: var(--dark); z-index: 9999; display: flex; flex-direction: column;
            justify-content: center; align-items: center; transition: 1s;
        }}
        .splash-hidden {{ opacity: 0; visibility: hidden; }}
        .splash-title {{ font-family: 'Great Vibes', cursive; font-size: 5rem; color: var(--gold); }}

        /* HERO */
        .hero {{
            height: 100vh; position: relative; display: flex;
            justify-content: center; align-items: center; overflow: hidden;
        }}
        .back-video {{ position: absolute; min-width: 100%; min-height: 100%; z-index: -1; object-fit: cover; }}
        .overlay {{ position: absolute; top:0; left:0; width:100%; height:100%; background: rgba(0,0,0,0.5); }}
        .hero-title {{ font-family: 'Great Vibes', cursive; font-size: 6rem; color: white; }}
        
        /* BOTONES SOCIALES */
        .social-sidebar {{ position: fixed; right: 20px; bottom: 30px; display: flex; flex-direction: column; gap: 15px; z-index: 1000; }}
        .social-btn {{ width: 55px; height: 55px; border-radius: 50%; color: white; display: flex; justify-content: center; align-items: center; font-size: 24px; text-decoration: none; transition: 0.3s; }}
        .float-wa {{ background: #25d366; animation: pulse 2s infinite; }}
        .float-ig {{ background: linear-gradient(45deg, #f09433, #cc2366, #bc1888); }}
        
        @keyframes pulse {{
            0% {{ box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }}
            70% {{ box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }}
            100% {{ box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }}
        }}
    </style>
</head>
<body>
    <div class="splash-screen" id="splash">
        <h1 class="splash-title">{INFO['nombre']}</h1>
        <p style="color: white; letter-spacing: 5px;">CARGANDO DULZURA...</p>
    </div>

    <div class="hero">
        <video autoplay muted loop playsinline class="back-video">
            <source src="https://assets.mixkit.co/videos/preview/mixkit-top-view-of-a-chocolate-cake-with-whipped-cream-14352-large.mp4" type="video/mp4">
        </video>
        <div class="overlay"></div>
        <div class="text-center position-relative" data-aos="zoom-in">
            <h1 class="hero-title">{INFO['nombre']}</h1>
            <p style="color: var(--gold); letter-spacing: 5px;">{INFO['ubicacion']}</p>
            <a href="{ws_link}" target="_blank" class="btn btn-lg px-5 mt-4 text-white" style="background: var(--gold); border-radius: 50px;">PEDIR AHORA</a>
        </div>
    </div>

    <div class="container py-5 text-center">
        <div data-aos="fade-up">
            <h2 style="font-family: 'Playfair Display'; text-transform: uppercase;">Nuestra Pasión</h2>
            <div style="width: 60px; height: 3px; background: var(--gold); margin: 20px auto;"></div>
            <p class="lead text-muted">{INFO['descripcion']}</p>
        </div>
        <div class="row mt-5">
            {servicios_html}
        </div>
    </div>

    <div class="py-5 bg-dark text-white text-center">
        <div class="container">
            <h2 class="mb-5">Experiencias Luli</h2>
            <div class="row">{testimonios_html}</div>
        </div>
    </div>

    <div class="social-sidebar">
        <a href="{ws_link}" class="social-btn float-wa" target="_blank"><i class="fab fa-whatsapp"></i></a>
        <a href="{INFO['instagram']}" class="social-btn float-ig" target="_blank"><i class="fab fa-instagram"></i></a>
    </div>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({{ duration: 1000 }});
        window.addEventListener('load', () => {{
            setTimeout(() => {{
                document.getElementById('splash').classList.add('splash-hidden');
            }}, 2000);
        }});
    </script>
</body>
</html>
"""

# Renderizar el HTML en Streamlit
components.html(html_final, height=2000, scrolling=False)
