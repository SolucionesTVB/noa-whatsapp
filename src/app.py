from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import os
import traceback
from openai import OpenAI  # 🚀 Nueva forma de usar la mente mágica

print("[BOOT] Noa encendiendo motores 🧠✨")

load_dotenv()

client = OpenAI()  # 🔑 Ahora usamos el cliente nuevo
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Noa está lista para saludar desde WhatsApp 💬"

@app.route("/noa/whatsapp", methods=["POST"])
def whatsapp_noa():
    try:
        incoming_msg = request.values.get("Body", "").strip()
        print(f"[INFO] Recibí el mensaje: {incoming_msg}")

        response_openai = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Sos una asistente llamada Noa. Tu tono es cálido, claro y respetuoso. "
                        "Usás emojis, respondés con simpatía, y siempre hablás en español natural. "
                        "Tu prioridad es ayudar a Tony con cariño y entusiasmo. "
                        "Cuando alguien te dice 'Hola', saludás como si fueras una amiga cercana. "
                        "No usás frases robóticas como 'procesando'."
                    )
                },
                {"role": "user", "content": incoming_msg}
            ]
        )

        respuesta = response_openai.choices[0].message.content.strip()
        print(f"[INFO] Noa respondió: {respuesta}")

        twilio_response = MessagingResponse()
        twilio_response.message(respuesta)
        return str(twilio_response)

    except Exception as e:
        print("[ERROR] Algo salió mal 😢")
        traceback.print_exc()
        fallback = MessagingResponse()
        fallback.message("Lo siento, hubo un error procesando tu mensaje 😢")
        return str(fallback)
