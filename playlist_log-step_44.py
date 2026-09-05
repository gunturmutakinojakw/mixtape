# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: PlaylistLog
import json, os

def backup_data(filepath, backup_dir="backups"):
    if not os.path.exists(filepath):
        return False
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = os.path.getmtime(filepath)
    name = f"{backup_dir}/playlist_log_{timestamp}.json"
    with open(name, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return name
