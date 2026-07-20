# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: PlaylistLog
def reset_demo_data():
    """Сбросить все сущности до пустых списков."""
    playlists = []
    tracks = []
    moods = ["happy", "chill", "energetic", "melancholic", "focused"]
    mood_tags = {}
    for mood in moods:
        mood_tags[mood] = {
            "name": mood.capitalize(),
            "description": f"Настроение {mood}",
            "tracks": [],
            "color": {"r": 180, "g": 200 + (hash(mood) % 55), "b": 80},
        }
    history = []
    stats = {}
    return playlists, tracks, moods, mood_tags, history, stats


def clear_state():
    """Полный сброс: демо-данные + история + статистика."""
    playlists, tracks, moods_list, mood_tags, history, stats = reset_demo_data()
    user_stats = {
        "total_played": 0,
        "most_listened_genre": None,
        "favorite_mood": None,
        "listening_days": set(),
    }
    return playlists, tracks, moods_list, mood_tags, history, stats, user_stats
