import reflex as rx

def footer():
    return rx.box(
        rx.vstack(
            rx.text("© 2023 LegalCorp - Asesoría Jurídica Integral", font_size="2"),
            rx.hstack(
                rx.link("Términos y Condiciones", href="#"),
                rx.link("Política de Privacidad", href="#"),
                rx.link("Contacto", href="#"),
                spacing="2",
            ),
            padding="2",
            bg="primary",
            color="white",
            align="center",
        ),
        width="100%",
    )