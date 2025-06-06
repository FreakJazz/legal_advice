import reflex as rx
from ..components import navbar, footer

class LegalResourcesState(rx.State):
    search_query: str = ""
    resources: list[dict] = [
        {
            "title": "Código Civil",
            "description": "Normas que regulan las relaciones privadas entre personas.",
            "link": "https://example.com/codigo-civil"
        },
        {
            "title": "Código Penal",
            "description": "Leyes que definen los delitos y sus penas.",
            "link": "https://example.com/codigo-penal"
        },
        {
            "title": "Ley del Trabajo",
            "description": "Normativa que regula las relaciones laborales.",
            "link": "https://example.com/ley-trabajo"
        },
        {
            "title": "Constitución Nacional",
            "description": "Ley fundamental que establece la organización del Estado.",
            "link": "https://example.com/constitucion"
        },
    ]
    
    @rx.var
    def filtered_resources(self) -> list[dict]:
        if not self.search_query:
            return self.resources
        return [res for res in self.resources 
                if self.search_query.lower() in res["title"].lower() 
                or self.search_query.lower() in res["description"].lower()]

def legal_resources():
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("Recursos Legales", size="1", margin_bottom="2"),
                rx.text(
                    "Accede a documentos legales y recursos gratuitos para tu información.",
                    margin_bottom="3",
                ),
                rx.input(
                    placeholder="Buscar recursos...",
                    on_change=LegalResourcesState.set_search_query,
                    width="100%",
                    margin_bottom="3",
                ),
                rx.vstack(
                    rx.foreach(
                        LegalResourcesState.filtered_resources,
                        lambda resource: rx.card(
                            rx.heading(resource["title"], size="4"),
                            rx.text(resource["description"], margin_top="2"),
                            rx.link(
                                rx.button("Ver documento", margin_top="2"),
                                href=resource["link"],
                                is_external=True,
                            ),
                            width="100%",
                        ),
                    ),
                    spacing="2",
                    width="100%",
                ),
                align="center",
                spacing="2",
            ),
            max_width="1200px",
            padding="3",
        ),
        footer(),
        min_height="100vh",
    )