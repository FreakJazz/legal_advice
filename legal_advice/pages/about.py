import reflex as rx
from ..components import navbar, footer

def about():
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("Sobre LegalCorp", size="1", margin_bottom="2"),
                rx.text(
                    "LegalCorp es una firma de abogados comprometida con la excelencia en el servicio legal.",
                    margin_bottom="2",
                ),
                rx.box(
                    rx.vstack(
                        rx.heading("Nuestra Historia", size="3"),
                        rx.text(
                            "Fundada en 2010, LegalCorp ha crecido de un pequeño bufete a una firma reconocida "
                            "nacionalmente por nuestro compromiso con los clientes y nuestra experiencia legal."
                        ),
                        rx.heading("Nuestro Equipo", size="3", margin_top="2"),
                        rx.text(
                            "Contamos con un equipo multidisciplinario de abogados especializados en diversas "
                            "áreas del derecho, garantizando soluciones integrales a nuestros clientes."
                        ),
                        rx.heading("Nuestra Misión", size="3", margin_top="2"),
                        rx.text(
                            "Proveer servicios legales de alta calidad, accesibles y éticos, ayudando a nuestros "
                            "clientes a navegar el complejo mundo legal con confianza."
                        ),
                        spacing="2",
                    ),
                    bg="white",
                    padding="2",
                    border_radius="lg",
                ),
                align="center",
                spacing="2",
            ),
            max_width="1200px",
            padding="2",
        ),
        footer(),
        min_height="100vh",
    )