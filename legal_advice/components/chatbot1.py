import reflex as rx

# Diccionario global de respuestas legales
legal_responses = {
    "contrato": {
        "preguntas": [
            "¿Qué es un contrato válido?",
            "¿Qué elementos debe tener un contrato?",
            "¿Puedo cancelar un contrato firmado?",
            "¿Qué pasa si incumplo un contrato?"
        ],
        "respuesta": """Un contrato válido requiere: 
1. Consentimiento libre de vicios
2. Objeto lícito posible
3. Causa lícita
Los elementos esenciales son: oferta, aceptación, capacidad legal y contraprestación. 
La cancelación depende de cláusulas de terminación. El incumplimiento puede generar indemnización."""
    },
    "divorcio": {
        "preguntas": [
            "¿Qué documentos necesito para divorciarme?",
            "¿Cómo se divide la propiedad en un divorcio?",
            "¿Cómo se determina la custodia?",
            "¿Cuánto tarda un divorcio?"
        ],
        "respuesta": """Proceso de divorcio:
1. Documentos: Acta matrimonial, identificación, inventario de bienes
2. La propiedad se divide según régimen matrimonial (50/50 en sociedad conyugal)
3. Custodia: Primero el interés superior del menor
4. Duración: 3-12 meses según tipo (unilateral/bilateral)"""
    },
    "despido": {
        "preguntas": [
            "¿Qué indemnización me corresponde por despido?",
            "¿Qué es un despido injustificado?",
            "¿Cómo reclamo mis beneficios?",
            "¿Tengo derecho a vacaciones no pagadas?"
        ],
        "respuesta": """En caso de despido:
- Indemnización: 3 meses de salario + 20 días por año
- Despido injustificado: Sin causa real/formal
- Reclamo: Mediación laboral o demanda
- Vacaciones: Deben pagarse proporcionalmente"""
    },
    "denuncia": {
        "preguntas": [
            "¿Cómo pongo una denuncia penal?",
            "¿Qué pruebas necesito?",
            "¿Cuánto tarda un proceso penal?",
            "¿Necesito abogado para denunciar?"
        ],
        "respuesta": """Proceso penal:
1. Denuncia: Fiscalía o policía (no necesita abogado)
2. Pruebas: Documentales, testimoniales, periciales
3. Duración: 1-3 años según complejidad
4. Asesoría legal recomendada para seguimiento"""
    }
}

class ChatState(rx.State):
    question: str = ""
    chat_history: list[tuple[str, str]] = []

    def answer(self):
        answer = self.answer_question()
        self.chat_history.append((self.question, answer))
        self.question = ""

    def answer_question(self):
        user_input = self.question.lower()
        for category, data in legal_responses.items():
            if category in user_input:
                answer = f"{data['respuesta']}\n\n¿Te gustaría saber más sobre:\n"
                answer += "\n".join([f"- {p}" for p in data['preguntas'][:3]])
                return answer

        # Si no encuentra una categoría
        answer = "¿Sobre qué área legal necesitas información? Puedo ayudarte con:\n"
        answer += "\n".join([f"- {key.capitalize()} ({len(value['preguntas'])} preguntas frecuentes)"
                             for key, value in legal_responses.items()])
        answer += "\n\nTambién puedes preguntarme directamente: '¿Qué necesito para...?'"
        return answer

def chatbot_manual():
    return rx.box(
        rx.vstack(
            rx.heading("Asistente Legal Virtual", size="4", margin_bottom="2"),
            rx.box(
                rx.foreach(
                    ChatState.chat_history,
                    lambda message: rx.vstack(
                        rx.text(f"Tú: {message[0]}", font_weight="bold"),
                        rx.text(f"Asistente: {message[1]}", color="text"),
                        spacing="1",
                        margin_bottom="2",
                    ),
                ),
                height="200px",
                overflow_y="auto",
                padding="2",
                border="1px solid #e2e8f0",
                border_radius="md",
                margin_bottom="2",
            ),
            rx.hstack(
                rx.input(
                    value=ChatState.question,
                    placeholder="Ejemplo: '¿Qué necesito para un divorcio?'",
                    on_change=ChatState.set_question,
                    width="100%",
                ),
                rx.button("Enviar", on_click=ChatState.answer, margin_left="2"),
                width="100%",
            ),
            width="100%",
            max_width="600px",
            margin_y="4",
            padding="4",
            bg="white",
            border_radius="lg",
            box_shadow="md",
        ),
        width="100%",
        display="flex",
        justify_content="center",
    )
