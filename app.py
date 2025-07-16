from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)

openai.api_key = "TU_API_KEY_AQUI"  # Reemplazá con tu clave real

@app.route("/noa/whatsapp", methods=["POST"])
def whatsapp_noa():
    mensaje = request.form.get("Body", "").strip()
    print(f"📩 Mensaje recibido: {mensaje}")  # Log para Render

    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sos Noa, una asistente que ayuda con documentos de aseguradoras en Costa Rica. Sé clara, amable y eficiente."},
                {"role": "user", "content": mensaje}
            ],
            temperature=0.7
        )
        texto = respuesta.choices[0].message.content.strip()
    except Exception as e:
        print(f"⚠️ Error interno: {e}")
        texto = "⚠️ Noa tuvo un problema al procesar tu mensaje. Intentá de nuevo."

    twilio_resp = MessagingResponse()
    twilio_resp.message(texto)
    return str(twilio_resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
