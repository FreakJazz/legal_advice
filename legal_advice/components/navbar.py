import reflex as rx

def navbar():
    return rx.box(
        rx.hstack(
            rx.heading("LegalCorp", size="3"),
            rx.spacer(),
            rx.hstack(
                rx.link("Inicio", href="/", _hover={"text_decoration": "underline"}),
                rx.link("Servicios", href="/servicios", _hover={"text_decoration": "underline"}),
                rx.link("Nosotros", href="/nosotros", _hover={"text_decoration": "underline"}),
                rx.link("Recursos Legales", href="/recursos-legales", _hover={"text_decoration": "underline"}),
                spacing="4",
                display=["none", "none", "flex", "flex", "flex"],
            ),
            justify="between", 
            width="100%",
            padding="4",
            bg="primary",
            color="white",
        ),
        position="sticky",
        top="0",
        z_index="1000",
    )