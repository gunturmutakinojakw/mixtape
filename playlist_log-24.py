# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: PlaylistLog
def print_record(record):
    """Compact single-record view."""
    if not record:
        return "No record."
    mood = record.get("mood", "")
    moods_str = ", ".join(mood) if isinstance(mood, list) else mood or ""
    lines = [
        f"🎵 {record['track']} — {record['album']}",
        f"   🕐 {record['time']}",
        f"   📁 Playlist: {record.get('playlist', '—')}",
        f"   🏷️ Mood: {moods_str or '—'}",
    ]
    print("\n".join(lines))
