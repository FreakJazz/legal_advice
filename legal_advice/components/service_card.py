import reflex as rx

def service_card(title, description):
    return rx.card(
        rx.heading(title, size="4"),
        rx.text(description, margin_top="2"),
        rx.button("Más información", margin_top="2"),
        width="100%",
        variant="ghost",
        _hover={
            "box_shadow": "lg",
            "transform": "translateY(-5px)",
            "transition": "all 0.3s ease",
        },
    )