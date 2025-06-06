import reflex as rx
from ..components.navbar import navbar
from ..components.footer import footer
from ..components.chatbot import chatbot
from ..components.chatbot1 import chatbot_manual

def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            rx.container(
                rx.vstack(
                    # Sección de presentación
                    rx.heading("Asesoría Legal Profesional", size="1", margin_bottom="4"),
                    rx.text(
                        "En LegalCorp brindamos soluciones jurídicas integrales para proteger tus intereses y garantizar el cumplimiento de la ley.",
                        margin_bottom="4",
                    ),
                    
                    # Sección de servicios
                    rx.grid(
                        rx.box(
                            rx.heading("Consultoría", size="3"),
                            rx.text("Asesoramiento legal personalizado para individuos y empresas."),
                            bg="white",
                            padding="4",
                            border_radius="lg",
                        ),
                        rx.box(
                            rx.heading("Documentación", size="3"),
                            rx.text("Elaboración y revisión de contratos, acuerdos y documentos legales."),
                            bg="white",
                            padding="4",
                            border_radius="lg",
                        ),
                        rx.box(
                            rx.heading("Representación", size="3"),
                            rx.text("Defensa legal en procedimientos judiciales y administrativos."),
                            bg="white",
                            padding="4",
                            border_radius="lg",
                        ),
                        columns="3",
                        spacing="4", 
                        margin_bottom="4",
                    ),
                    
                    # Botón de servicios
                    rx.link(
                        rx.button("Conoce nuestros servicios", size="3"),
                        href="/servicios",
                        margin_bottom="8",
                    ),
                    
                    # Primer chatbot
                    rx.heading("Asistente Virtual Automático", size="3", margin_bottom="2"),
                    rx.text(
                        "Responde automáticamente a preguntas comunes sobre temas legales", 
                        margin_bottom="4"
                    ),
                    chatbot(),
                    
                    # Segundo chatbot manual
                    rx.heading("Asistente con Abogados", size="3", margin_bottom="2", margin_top="8"),
                    rx.text(
                        "Conéctate con nuestros especialistas para consultas personalizadas", 
                        margin_bottom="4"
                    ),
                    chatbot_manual(),
                    
                    align="center",
                    spacing="4",
                ),
                max_width="1200px",
                padding="4",
                margin_top="16px",
            ),
            footer(),
            min_height="100vh",
            position="relative",
        ),
        width="100%",
    )