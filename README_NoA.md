# 📁 Proyecto Noa – Asistente de pólizas de seguros (Costa Rica)

Un dashboard inteligente que transforma un Excel de SUGESE en una tabla web interactiva, estilizada, con botones reales de descarga y actualizada automáticamente con respaldo.

---

## ✅ Estado actual del proyecto

- ✔️ Flask funcionando en `app.py`
- ✔️ Excel leído dinámicamente desde `sugeseM_datos.xlsx`
- ✔️ Extracción automática de hipervínculos ocultos
- ✔️ Enlaces convertidos en botones `📄 Ver PDF`
- ✔️ Diseño estilizado en `style.css`
- ✔️ Copias de seguridad automáticas (`resguardo.py`)
- ✔️ Tabla HTML funcional desde `tabla.html`

---

## 📂 Estructura del proyecto


---

## 🚧 Próximos pasos

| Prioridad | Tarea                                                                 |
|-----------|------------------------------------------------------------------------|
| 🔜 Alta    | Validar que todos los enlaces de descarga funcionen correctamente     |
| 🧠 Media   | Detectar tipo de archivo (.pdf, .docx, .xlsx) y cambiar ícono del botón |
| 🗃️ Media   | Agregar filtros y búsqueda con DataTables.js                          |
| 🔄 Media   | Automatizar renombramiento si el Excel de SUGESE cambia de nombre     |
| 📩 Baja    | Opción para exportar la tabla como Excel o PDF                        |
| ☁️ Futuro | Subir Noa a la nube (ej. Render, PythonAnywhere, etc.)                |

---

## 🤖 Notas técnicas útiles

- Usamos `openpyxl` para leer los hipervínculos reales, ya que `pandas` solo lee el texto visible.
- El estilo de los botones está en `style.css` bajo `.boton-descarga`.
- Los enlaces vacíos se muestran como: `— No disponible —`
- Cada ejecución genera un respaldo automático del Excel en `/backups`.

---

## ✨ Autores

- 🧠 Diseño, conceptualización y pruebas: **Tony**
- 🤖 Apoyo técnico y asistencia creativa: **Copilot**
