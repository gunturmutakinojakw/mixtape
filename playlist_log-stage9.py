# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: PlaylistLog
import json, uuid, random, datetime as dt
from typing import Dict, List, Any

INITIAL_DATA = '''
{
  "users": [
    {"id": "u1", "name": "Алексей", "created_at": "2024-01-01T00:00:00Z"},
    {"id": "u2", "name": "Мария", "created_at": "2024-01-02T00:00:00Z"}
  ],
  "moods": ["Happy", "Sad", "Energetic", "Calm"],
  "tracks": [
    {"id": "t1", "title": "Bohemian Rhapsody", "artist": "Queen", "duration_sec": 354},
    {"id": "t2", "title": "Imagine", "artist": "John Lennon", "duration_sec": 183}
  ],
  "playlists": [
    {"id": "p1", "name": "Rock Classics", "owner_id": "u1"},
    {"id": "p2", "name": "Chill Vibes", "owner_id": "u2"}
  ]
}'''

def load_initial_data() -> Dict[str, Any]:
    try:
        data = json.loads(INITIAL_DATA)
        # Присваиваем UUID трекам и плейлистам для уникальности в БД/файле
        for track in data.get("tracks", []):
            if "uuid" not in track:
                track["uuid"] = str(uuid.uuid4())
        for playlist in data.get("playlists", []):
            if "uuid" not in playlist:
                playlist["uuid"] = str(uuid.uuid4())
        # Генерируем историю прослушивания для демо-данных (не более 5 записей на пользователя)
        history_records: List[Dict[str, Any]] = []
        for user in data.get("users", []):
            count = random.randint(0, 5)
            for _ in range(count):
                mood = random.choice(data.get("moods", []))
                track_ref = random.choice(data.get("tracks", []))
                history_records.append({
                    "user_id": user["id"],
                    "track_uuid": track_ref["uuid"],
                    "playlist_uuid": None, # Пока без привязки к плейлисту в истории
                    "mood": mood,
                    "played_at": (dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=random.randint(1, 72))).isoformat(),
                    "duration_sec": track_ref.get("duration_sec", 0),
                    "position_in_playlist": random.randint(1, 10)
                })
        data["history"] = history_records
        return data
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга начальных данных: {e}")
        raise
