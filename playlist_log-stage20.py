# === Stage 20: Добавь восстановление записей из архива ===
# Project: PlaylistLog
import json, os

ARCHIVE_FILE = "playlistlog_archive.json"

def restore_from_archive():
    if not os.path.exists(ARCHIVE_FILE):
        return []
    try:
        with open(ARCHIVE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        records = data.get("records", [])
        for rec in records:
            if "timestamp" not in rec or rec["timestamp"] is None:
                continue
            try:
                rec["timestamp"] = int(rec["timestamp"])
            except (ValueError, TypeError):
                continue
            print(f"[ARCHIVE] Restored {rec.get('type', 'unknown')} at {rec['timestamp']}")
        return records
    except Exception as e:
        print(f"[ERROR] Failed to restore archive: {e}")
        return []

def save_to_archive(records):
    os.makedirs("archive", exist_ok=True)
    with open(os.path.join("archive", ARCHIVE_FILE), 'w', encoding='utf-8') as f:
        json.dump({"records": records}, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    restored = restore_from_archive()
    if restored:
        save_to_archive(restored)
