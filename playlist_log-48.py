# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: PlaylistLog
def _clean_title(text):
    return text.strip().title() if text else text

def _parse_duration(text):
    parts = text.split()
    if not parts:
        return 0
    seconds = 0
    for part in parts:
        if part.endswith('s'):
            seconds += int(part[:-1])
        elif part.endswith('min'):
            seconds += int(part[:-3]) * 60
        elif part.endswith('h'):
            seconds += int(part[:-1]) * 3600
        else:
            try:
                seconds += int(part)
            except ValueError:
                pass
    return seconds
