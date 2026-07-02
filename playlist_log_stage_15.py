# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: PlaylistLog
def calculate_weekly_stats(history):
    from datetime import datetime, timedelta
    if not history: return {}
    grouped = {}
    for entry in history:
        date_str = entry.get('date') or entry.get('timestamp', '')
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            week_start = (dt - timedelta(days=dt.weekday())).strftime('%Y-%W')
        except Exception: continue
        key = f"{week_start}:{entry.get('playlist_name', 'unknown')}:{entry.get('mood', 'neutral')}"
        grouped[key] = grouped.get(key, 0) + 1
    return dict(sorted(grouped.items()))
