import reflex as rx
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatState(rx.State):
    question: str = ""
    chat_history: list[tuple[str, str]] = []

    def answer(self):
        # Respuesta usando IA (OpenAI)
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "Eres un asistente legal que proporciona información general sobre temas legales. No des asesoría legal específica.",
                    },
                    {"role": "user", "content": self.question},
                ],
                temperature=0.5,
                max_tokens=500,
            )
            answer = response.choices[0].message["content"].strip()
        except Exception as e:
            answer = "Ocurrió un error al obtener la respuesta. Por favor, intenta más tarde."

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
                "transform": "translateY(-5px)"
            }
        }
    )
