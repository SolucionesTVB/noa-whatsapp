#!/bin/bash
echo "🔥 Iniciando Noa en el puerto 5050..."
python3 app.py &
sleep 2
open http://127.0.0.1:5050/
