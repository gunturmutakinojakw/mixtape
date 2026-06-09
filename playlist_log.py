# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: PlaylistLog
import json
from datetime import datetime
from typing import Dict, List, Any

class PlaylistLog:
    def __init__(self):
        self.data: Dict[str, Any] = {
            "playlists": {},
            "history": [],
            "settings": {"theme": "dark", "language": "ru"}
        }
        self._save()

    def _save(self) -> None:
        with open("playlist_log.json", "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def add_track(self, playlist_name: str, track_info: Dict[str, Any]) -> None:
        if playlist_name not in self.data["playlists"]:
            self.data["playlists"][playlist_name] = []
        entry = {**track_info, "timestamp": datetime.now().isoformat()}
        self.data["playlists"][playlist_name].append(entry)
        self._save()

    def add_history(self, action: str, details: Dict[str, Any]) -> None:
        self.data["history"].append({
            "action": action,
            "details": details,
            "timestamp": datetime.now().isoformat()
        })
        self._save()

# Демонстрационные данные и запуск
if __name__ == "__main__":
    log = PlaylistLog()
    
    # Добавляем плейлист
    log.add_track("Вечерний джаз", {
        "artist": "Miles Davis",
        "title": "So What",
        "album": "Kind of Blue",
        "duration_seconds": 562,
        "mood": "relaxed"
    })
    
    # Добавляем историю прослушивания
    log.add_history("track_played", {
        "playlist": "Вечерний джаз",
        "track": "So What",
        "position": 1
    })
    
    print("Инициализация PlaylistLog завершена. Данные сохранены в playlist_log.json")
