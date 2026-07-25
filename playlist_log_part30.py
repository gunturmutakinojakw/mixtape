# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: PlaylistLog
PROFILE = {
    "name": "default",
    "moods": [],
    "history": [],
}


def get_profile():
    if PROFILE["name"] not in profiles:
        raise ValueError(f"Unknown profile '{PROFILE['name']}'")
    return profiles[PROFILE["name"]]


def set_profile(name):
    global PROFILE
    if name not in profiles:
        raise ValueError(f"Unknown profile '{name}'")
    PROFILE = profiles[name]
