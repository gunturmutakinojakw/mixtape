# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: PlaylistLog
import json, os

DATA_FILE = "playlist_log.json"

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"playlists": [], "tracks": [], "moods": {}, "history": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"playlists": [], "tracks": [], "moods": {}, "history": []}

def add_track(track_data):
    data = load_data()
    track_id = len(data["tracks"]) + 1
    track_entry = {
        "id": track_id,
        **track_data,
        "timestamp": datetime.now().isoformat(),
        "mood": track_data.get("mood", None)
    }
    data["tracks"].append(track_entry)
    if track_data.get("playlist_name"):
        playlist = next((p for p in data["playlists"] if p["name"] == track_data["playlist_name"]), None)
        if playlist:
            playlist["track_ids"].append(track_id)
    save_data(data)
    return track_entry

def add_mood(mood_name, description):
    data = load_data()
    mood_id = len(data["moods"]) + 1
    data["moods"][mood_name] = {
        "id": mood_id,
        "description": description
    }
    save_data(data)

def add_history_entry(track_id, duration_seconds):
    data = load_data()
    entry = {"track_id": track_id, "duration": duration_seconds}
    data["history"].append(entry)
    save_data(data)
