# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: PlaylistLog
def generate_summary():
    if not tracks: return "Данные пусты."
    total_time = sum(t.duration for t in tracks) / 3600
    moods = set(t.mood for t in tracks)
    top_artist = max(set(t.artist for t in tracks), key=lambda a: len([t for t in tracks if t.artist == a]), default="")
    print(f"Треков: {len(tracks)} | Время: {total_time:.1f}ч | Настроения: {', '.join(sorted(moods))} | Топ-исполнитель: {top_artist}")
