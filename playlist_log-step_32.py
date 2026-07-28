# === Stage 32: Добавь журнал действий пользователя ===
# Project: PlaylistLog
class ActionLogger:
    def __init__(self):
        self.actions = []
    
    def log(self, action_type, details=None):
        self.actions.append({
            'type': action_type,
            'details': details or {},
            'timestamp': datetime.now().isoformat()
        })
    
    def get_recent(self, limit=10):
        return self.actions[-limit:]
    
    def summary(self):
        counts = {}
        for a in self.actions:
            t = a['type']
            counts[t] = counts.get(t, 0) + 1
        return counts

logger = ActionLogger()
