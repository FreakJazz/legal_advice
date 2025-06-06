import reflex as rx

SERVICIOS = [
    "Asesoría en contratos",
    "Consultoría legal empresarial",
    "Defensa en litigios civiles",
    "Asesoría en propiedad intelectual",
]

PRODUCTOS = [
    "Plantillas de contratos personalizables",
    "Guías legales descargables",
    "Software de gestión legal",
]

INFORMACION_LEGAL = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

def chatbot_response(user_input: str) -> str:
    user_input = user_input.lower()
    if "contrato" in user_input:
        return "Los contratos deben ser claros y proteger tus derechos. ¿Quieres que te ayude con un modelo?"
    elif "litigio" in user_input:
        return "El litigio es un proceso legal para resolver disputas. ¿Necesitas asistencia específica?"
    elif "propiedad intelectual" in user_input:
        return "La propiedad intelectual protege tus creaciones. ¿Quieres saber más?"
    else:
        return "Gracias por tu pregunta, un asesor se pondrá en contacto contigo pronto."

class State(rx.State):
    chat_history: list[tuple[str, str]] = []

    input_text: str = ""

    def send_message(self):
        if not self.input_text.strip():
            return
        user_msg = self.input_text.strip()
        if "contrato" in user_msg.lower():
            bot_msg = "Los contratos deben ser claros y proteger tus derechos."
        elif "litigio" in user_msg.lower():
            bot_msg = "El litigio es un proceso legal para resolver disputas."
        else:
            bot_msg = "Gracias por tu pregunta, un asesor se pondrá en contacto contigo pronto."

        self.chat_history.append(("Tú", user_msg))
        self.chat_history.append(("Bot", bot_msg))

        self.input_text = ""

def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Corporación Asesoría Legal", size="3", mb=4),

            rx.box(
                rx.heading("Servicios que ofrecemos", size="2"),
                rx.unordered_list([rx.list_item(s) for s in SERVICIOS]),
                mb=4,
            ),

            rx.box(
                rx.heading("Productos disponibles", size="2"),
                rx.unordered_list([rx.list_item(p) for p in PRODUCTOS]),
                mb=4,
            ),

            rx.box(
                rx.heading("Información legal", size="2"),
                rx.text(INFORMACION_LEGAL),
                mb=8,
            ),

            rx.box(
                rx.heading("Chat de Asesoría Legal", size="2", mb=3),
                rx.vstack(
                    rx.foreach(
                        State.chat_history.to(list[tuple[str, str]]),
                        lambda item, i: rx.text(f"{item[0]}: {item[1]}", key=f"{i}", padding="0.25rem 0")
                    ),
                    max_height="200px",
                    overflow_y="auto",
                    mb=3,
                    border="1px solid",
                    border_color="gray.300",
                    padding="0.5rem",
                    border_radius="md",
                ),
                rx.hstack(
                    rx.input(
                        placeholder="Escribe tu pregunta legal...",
                        value=State.input_text,
                        on_change=State.set_input_text,
                        flex=1,
                        on_key_down=lambda e: State.send_message() if e.key == "Enter" else None,
                    ),
                    rx.button("Enviar", on_click=State.send_message, ml=2),
                ),
                id="chatbot",
                mb=10,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
        padding="1rem",
        max_width="600px",
        margin="auto",
    )


app = rx.App()
app.add_page(index, title="Asesoría Legal")

# No se llama app.compile() ni app._compile()

