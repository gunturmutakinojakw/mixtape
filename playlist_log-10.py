# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: PlaylistLog
def export_to_json():
    import json
    from datetime import datetime
    state = {
        "version": 1,
        "timestamp": datetime.utcnow().isoformat(),
        "playlists": playlists,
        "tracks": tracks,
        "moods": moods,
        "history": history
    }
    return json.dumps(state, indent=2, ensure_ascii=False)
