# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: PlaylistLog
def migrate_to_v2(data):
    if data.get('version') != 2:
        if data.get('version') != 1 and 'version' not in data:
            data['version'] = 2
            data.setdefault('version_history', [])
            data['version_history'].append({
                'from': 1,
                'to': 2,
                'description': 'Added version tracking and migration support',
                'timestamp': time.time()
            })
        return data
    return data
