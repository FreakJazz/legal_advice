import reflex as rx
from ..components import navbar
from ..components import footer
from ..components.service_card import service_card

def services():
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("Nuestros Servicios Legales", size="1", margin_bottom="2"),
                rx.text(
                    "Ofrecemos una gama completa de servicios jurídicos para satisfacer tus necesidades legales.",
                    margin_bottom="3",
                ),
                rx.grid(
                    service_card(
                        "Derecho Civil",
                        "Contratos, obligaciones, responsabilidad civil, propiedad y sucesiones."
                    ),
                    service_card(
                        "Derecho Laboral",
                        "Despidos, contratación, conflictos laborales y asesoramiento a empresas."
                    ),
                    service_card(
                        "Derecho de Familia",
                        "Divorcios, custodia, adopción y alimentos."
                    ),
                    service_card(
                        "Derecho Penal",
                        "Defensa en procesos penales, asesoramiento a víctimas y recursos."
                    ),
                    service_card(
                        "Derecho Mercantil",
                        "Constitución de empresas, fusiones, adquisiciones y contratos comerciales."
                    ),
                    service_card(
                        "Derecho Inmobiliario",
                        "Compraventa, arrendamientos, hipotecas y reclamaciones de propiedad."
                    ),
                    columns="2",
                    spacing="2",
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