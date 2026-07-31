# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: PlaylistLog
TEMPLATES = {
    "morning": {"mood": "energetic", "genre": "pop", "note": "Morning vibes"},
    "workout": {"mood": "intense", "genre": "rock", "note": "Gym session"},
    "chill": {"mood": "relaxed", "genre": "jazz", "note": "Relaxing evening"},
}


def add_from_template(template_name, track_title=None):
    if template_name not in TEMPLATES:
        print(f"Unknown template: {template_name}")
        return None
    base = TEMPLATES[template_name]
    entry = {
        "mood": base["mood"],
        "genre": base["genre"],
        "note": f"{base['note']}, {track_title or 'untitled'}",
        "track_count": 0,
        "created_at": datetime.now().isoformat(),
    }
    if track_title:
        entry["tracks"] = [track_title]
    else:
        entry["tracks"] = []
    return entry


def log_entry(entry):
    global log_entries
    if isinstance(entry, dict) and "mood" in entry:
        log_entries.append(entry)
        print(f"[OK] Logged {entry['note'][:30]}...")
        return True
    elif isinstance(entry, str):
        log_entries.append({"raw": entry, "created_at": datetime.now().isoformat()})
        print(f"[OK] Raw note: {entry}")
        return True
    return False


def get_entry_history(mood=None):
    results = []
    for e in reversed(log_entries):
        if isinstance(e, dict) and "mood" in e:
            if mood is None or e["mood"] == mood:
                results.append(e)
        elif isinstance(e, str):
            results.append({"raw": e})
    return results
