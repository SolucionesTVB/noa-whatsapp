from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)

import os
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/noa/whatsapp", methods=["POST"])
def whatsapp_noa():
    mensaje = request.form.get("Body", "").strip()
    print(f"Mensaje recibido: {mensaje}")  # Log para Render

    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sos Noa, una asistente que ayuda con ..."},
                {"role": "user", "content": mensaje}
            ]
        )
        respuesta_texto = respuesta["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error: {e}")
        respuesta_texto = "Lo siento, hubo un error procesando tu mensaje."

    twilio_resp = MessagingResponse()
    twilio_resp.message(respuesta_texto)
    return str(twilio_resp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
