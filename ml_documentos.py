from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import joblib

# 📄 Datos simulados
titulos = [
    "Solicitud de seguro de vida",
    "Condiciones generales del seguro de auto",
    "Póliza Incendio de Todo Riesgo",
    "Endoso por cambio de beneficiario",
    "Resumen de cobertura",
    "Formulario de solicitud médica",
    "Póliza individual",
    "Endoso de cancelación",
    "Documento informativo"
]

tipos = [
    "solicitud",
    "condiciones",
    "póliza",
    "endoso",
    "otro",
    "solicitud",
    "póliza",
    "endoso",
    "otro"
]

# 🔠 Vectorización
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(titulos)

# 🧠 Modelo
modelo = MultinomialNB()
modelo.fit(X, tipos)

# 🔍 Pruebas de evaluación
frases_prueba = [
    "Formulario de seguro",
    "Condiciones generales de incendio",
    "Endoso por cambio de dirección",
    "Póliza de salud",
    "Documento de respaldo"
]

tipos_esperados = [
    "solicitud",
    "condiciones",
    "endoso",
    "póliza",
    "otro"
]

X_test = vectorizador.transform(frases_prueba)
predicciones = modelo.predict(X_test)

# 📊 Evaluación
print("🔍 Evaluación del modelo:")
for frase, pred, real in zip(frases_prueba, predicciones, tipos_esperados):
    print(f"🧠 '{frase}' → Predicho: {pred} | Esperado: {real}")

accuracy = accuracy_score(tipos_esperados, predicciones)
print(f"\n✅ Precisión del modelo: {accuracy:.2f}")

# 💾 Guardar modelo y vectorizador
joblib.dump(modelo, "modelo_documentos.pkl")
joblib.dump(vectorizador, "vectorizador_documentos.pkl")
print("\n📦 Modelo y vectorizador guardados.")
