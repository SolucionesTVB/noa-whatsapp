from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import os
import openai

print("[BOOT] app.py cargado correctamente 🔥")

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Noa está lista para responder por WhatsApp 💬"

@app.route("/noa/whatsapp", methods=["POST"])
def whatsapp_noa():
    try:
        incoming_msg = request.values.get("Body", "").strip()
        print(f"[INFO] Mensaje recibido: {incoming_msg}")

        print(f"[INFO] Clave OpenAI cargada: {'Sí' if openai.api_key else 'No'}")

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sos una asistente cálida llamada Noa."},
                {"role": "user", "content": incoming_msg}
            ]
        )
        respuesta = completion.choices[0].message.content.strip()
        print(f"[INFO] Respuesta generada: {respuesta}")

        response = MessagingResponse()
        response.message(respuesta)
        return str(response)

    except Exception as e:
        import traceback
        print("[ERROR] Fallo inesperado:")
        traceback.print_exc()
        fallback = MessagingResponse()
        fallback.message("Lo siento, hubo un error procesando tu mensaje 😢")
        return str(fallback)
