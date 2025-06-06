import reflex as rx

# Paleta de colores profesional
COLORS = {
    "primary": "#2C3E50",  # Azul oscuro
    "secondary": "#E74C3C",  # Rojo
    "accent": "#3498DB",  # Azul claro
    "background": "#F8F9FA",  # Gris claro
    "text": "#181717",
}

BASE_STYLE = {
    rx.button: {
        "background_color": COLORS["primary"],
        "color": "white",
        "_hover": {
            "background_color": COLORS["accent"],
        },
    },
    rx.heading: {
        "color": COLORS["primary"],
        "font_family": "Arial, sans-serif",
    },
    rx.text: {
        "color": COLORS["text"],
        "font_family": "Arial, sans-serif",
    },
    "background_color": COLORS["background"],
}

STYLE_SHEETS = [
    "https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap",
]