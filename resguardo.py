from datetime import datetime
from pathlib import Path
import shutil

def hacer_backup(archivo_path):
    """
    Crea una copia de seguridad del archivo recibido, con timestamp.

    Ej: sugesem_datos.xlsx -> backups/sugesem_datos_20250706_1124.xlsx
    """
    archivo = Path(archivo_path)

    if not archivo.exists():
        print(f"⚠️ Archivo no encontrado para backup: {archivo}")
        return

    backup_dir = Path("backups")
    backup_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nuevo_nombre = f"{archivo.stem}_{timestamp}{archivo.suffix}"
    destino = backup_dir / nuevo_nombre

    shutil.copy(archivo, destino)
    print(f"✅ Backup creado: {destino}")
