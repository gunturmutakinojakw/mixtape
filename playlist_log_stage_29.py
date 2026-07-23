# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: PlaylistLog
APP_CONFIG = {
    "app_name": "PlaylistLog",
    "version": 1,
    "max_tracks_per_playlist": 50,
    "track_duration_unit": "seconds",
    "mood_categories": ["happy", "sad", "energetic", "chill", "focus"],
    "default_mood": None,
    "history_limit_days": 7,
}

def get_config(key):
    return APP_CONFIG.get(key)

class Config:
    def __init__(self, cfg=None):
        if cfg is None:
            cfg = APP_CONFIG.copy()
        self.cfg = cfg

    def set(self, key, value):
        self.cfg[key] = value

    def get(self, key, default=None):
        return self.cfg.get(key, default)

    @classmethod
    def from_dict(cls, data):
        c = cls()
        for k, v in data.items():
            if isinstance(v, dict):
                setattr(c, k, cls.from_dict(v))
            else:
                setattr(c, k, v)
        return c

    @classmethod
    def from_file(cls, path):
        import json
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return cls.from_dict(data)

    def to_dict(self):
        d = {}
        for k in self.cfg:
            v = getattr(self, k, None)
            if isinstance(v, dict):
                d[k] = v.to_dict()
            else:
                d[k] = v
        return d
