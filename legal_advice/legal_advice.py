import reflex as rx
from .pages.index import index 
from .pages.services import services
from .pages.about import about
from .pages.legal_resources import legal_resources
from .styles import STYLE_SHEETS, BASE_STYLE

# Crear la aplicación
app = rx.App(
    style=BASE_STYLE,
    stylesheets=STYLE_SHEETS,
)

# Añadir las páginas
app.add_page(index, route="/")
app.add_page(services, route="/servicios")
app.add_page(about, route="/nosotros")
app.add_page(legal_resources, route="/recursos-legales")
