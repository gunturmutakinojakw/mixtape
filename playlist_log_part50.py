# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: PlaylistLog
def format_log_entry(entry: dict) -> str:
    """Форматирует запись прослушивания в читаемый строковый вид."""
    time_str = entry.get("time", "???:??").strftime("%H:%M") if isinstance(entry.get("time"), datetime) else str(entry.get("time", "???:??"))
    track = entry.get("track", {}).get("title", "Неизвестный трек")
    mood = entry.get("mood", {}).get("name", "Без настроения")
    duration = entry.get("duration", 0)
    if duration > 0:
        minutes, seconds = divmod(int(duration), 60)
        duration_str = f"{minutes}:{seconds:02d}"
    else:
        duration_str = "N/A"
    return f"[{time_str}] {track} | {mood} | {duration_str}"
