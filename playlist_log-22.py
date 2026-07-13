# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: PlaylistLog
def check_overdue_reminders():
    """Проверяет, есть ли просроченные напоминания."""
    overdue = []
    now = datetime.now()
    for reminder in reminders:
        if reminder["is_active"]:
            end_date = datetime.fromisoformat(reminder["end_date"])
            if now > end_date and now < datetime.fromisoformat(reminder["start_date"]):
                overdue.append({**reminder, "overdue_days": (now - end_date).days})
    reminders = [r for r in reminders if not r["is_active"]]
    return overdue
