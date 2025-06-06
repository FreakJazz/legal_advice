import reflex as rx

class ChatState(rx.State):
    question: str = ""
    chat_history: list[tuple[str, str]] = []

    def answer(self):
        # Respuestas predefinidas del chatbot
        legal_responses = {
            "contrato": "Un contrato es un acuerdo legal entre partes que crea obligaciones exigibles. Debe contener: oferta, aceptación, consideración y capacidad legal de las partes.",
            "divorcio": "El proceso de divorcio varía por jurisdicción. Generalmente requiere presentar una petición, notificar a la otra parte, resolver asuntos de custodia, manutención y división de bienes.",
            "herencia": "Las leyes de herencia determinan cómo se distribuyen los bienes de una persona fallecida. Si hay testamento, generalmente se sigue; si no, se aplican las leyes de sucesión intestada.",
            "laboral": "Los derechos laborales básicos incluyen salario mínimo, horas extras, condiciones seguras de trabajo y protección contra despido injustificado. Varían por país.",
        }
        
        # Buscar palabras clave en la pregunta
        answer = "Lo siento, no puedo proporcionar asesoría legal específica. Para consultas complejas, recomiendo contactar a un abogado certificado. "
        answer += "Puedo ofrecer información general sobre: contratos, divorcio, herencia o temas laborales."
        
        for key in legal_responses:
            if key in self.question.lower():
                answer = legal_responses[key]
                break
        
        self.chat_history.append((self.question, answer))
        self.question = ""

def chatbot():
    return rx.box(
        rx.vstack(
            rx.heading("Asistente Legal", size="4"),
            rx.box(
                rx.foreach(
                    ChatState.chat_history,
                    lambda message: rx.vstack(
                        rx.text(f"Tú: {message[0]}", align="left", width="100%"),
                        rx.text(f"Asistente: {message[1]}", align="left", width="100%", color="accent"),
                        spacing="2",
                        width="100%",
                    ),
                ),
                height="300px",
                overflow_y="auto",
                margin_bottom="2",
            ),
            rx.hstack(
                rx.input(
                    value=ChatState.question,
                    placeholder="Haz una pregunta legal...",
                    on_change=ChatState.set_question,
                    width="100%",
                ),
                rx.button("Enviar", on_click=ChatState.answer),
                width="100%",
            ),
            bg="white",
            padding="2",
            border_radius="lg",
            box_shadow="md",
        ),
      position="fixed",
        bottom="4",
        right="4",
        z_index="1000",
        style={
            "transform": "translateY(0)",
            "transition": "transform 0.3s ease",
            "_hover": {
                "transform": "translateY(-1px)"
            }
        }
    )