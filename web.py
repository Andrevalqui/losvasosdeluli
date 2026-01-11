import os
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

# DATOS DE LA EMPRESA DE POSTRES
INFO = {
    "nombre": "Los Vasos de Luli",
    "ubicacion": "Repostería Artesanal",
    "descripcion": "Transformamos ingredientes seleccionados en obras de arte comestibles. Especialistas en repostería fina de autor para momentos inolvidables.",
    "precio": "Ver Catálogo PDF",
    "whatsapp": "51977905037",
    "mapa_link": "https://www.google.com/maps", # Opcional: Link a tu local
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

@app.route('/')
def home():
    carpeta_img = os.path.join(app.root_path, 'static', 'img')
    if not os.path.exists(carpeta_img): os.makedirs(carpeta_img)
    archivos = os.listdir(carpeta_img)
    ext_validas = ('.jpg', '.jpeg', '.png', '.webp')
    galeria = [img for img in archivos if img.lower().endswith(ext_validas)]
    
    mensaje = f"Hola, vi la web de {INFO['nombre']} y quisiera el catálogo de postres."
    ws_link = f"https://wa.me/{INFO['whatsapp']}?text={mensaje.replace(' ', '%20')}"
    
    return render_template('index.html', 
                           info=INFO, 
                           servicios=SERVICIOS, 
                           reviews=TESTIMONIOS, 
                           galeria=galeria,
                           ws_link=ws_link,
                           anio=datetime.now().year)

if __name__ == '__main__':
    app.run()