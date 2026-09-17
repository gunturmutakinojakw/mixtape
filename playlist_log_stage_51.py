# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: PlaylistLog
class ChangeLog:
    def __init__(self):
        self.entries = []

    def log(self, action, entity, details):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "entity": entity,
            "details": details,
        }
        self.entries.append(entry)

    def get_entries(self, limit=10):
        return self.entries[-limit:]
