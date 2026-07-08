# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: PlaylistLog
def archive_records(records, max_age_days=365):
    """Archive records older than `max_age_days` days."""
    from datetime import datetime, timedelta
    cutoff = (datetime.now() - timedelta(days=max_age_days)).isoformat()
    archived = [r for r in records if r.get("created_at", "").split(".")[0] < cutoff]
    active = [r for r in records if r not in archived]
    return {"archived": archived, "active": active}
