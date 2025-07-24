from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Noa está lista para saludar desde WhatsApp 💬", 200

@app.route("/whatsapp", methods=["POST"])
def whatsapp_noa():
    texto_usuario = request.form.get("Body")
    print("[DEBUG] Texto recibido:", texto_usuario)

    respuesta = f"Noa responde: {texto_usuario}"
    twilio_response = MessagingResponse()
    twilio_response.message(respuesta)

    return str(twilio_response)
