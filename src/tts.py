import os
import requests
from dotenv import load_dotenv

load_dotenv()

def generar_audio(texto):
    elevenlabs_key = os.getenv("ELEVENLABS_API_KEY")
    print("[DEBUG] Clave ElevenLabs:", elevenlabs_key)

    voice_id = "EXAVITQu4vr4xnSDxMaL"
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": elevenlabs_key,
        "Content-Type": "application/json"
    }

    texto = texto[:150]

    data = {
        "text": texto,
        "voice_settings": {
            "stability": 0.3,
            "similarity_boost": 0.3
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("[DEBUG] Audio recibido de ElevenLabs ✅")

        audio_path = os.path.join(os.path.dirname(__file__), "static", "respuesta_noa.mp3")
        try:
            with open(audio_path, "wb") as f:
                f.write(response.content)
            print("[DEBUG] Audio guardado en:", audio_path)

            dominio = os.getenv("PUBLIC_URL")
            url_final = f"{dominio}/static/respuesta_noa.mp3"
            print("[DEBUG] Resultado final:", url_final)
            return url_final

        except Exception as e:
            print("[ERROR] No se pudo guardar el audio:", str(e))
            return None
    else:
        print("[DEBUG] Audio generation failed. Status:", response.status_code)
        print("[DEBUG] Response:", response.text)
        return None
