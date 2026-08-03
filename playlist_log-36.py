# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: PlaylistLog
def verify_integrity_and_fix(data):
    """Проверяет целостность данных и пытается исправить типичные проблемы."""
    if not isinstance(data, dict) or 'tracks' not in data:
        return {'status': 'error', 'message': 'Некорректный формат данных'}
    
    fixed_count = 0
    
    # Проверяем треки
    for i, track in enumerate(data['tracks']):
        if isinstance(track, dict):
            # Исправляем отсутствие id
            if 'id' not in track:
                track['id'] = f"track_{i}"
                fixed_count += 1
            
            # Исправляем пустой name
            if not track.get('name'):
                track['name'] = "Без названия"
                fixed_count += 1
            
            # Исправляем отсутствие длительности
            if 'duration' not in track:
                track['duration'] = 0
                fixed_count += 1
        
        elif isinstance(track, str) and len(track.strip()) > 3:
            data['tracks'].append({'id': f"track_{i}", 'name': track.strip(), 'duration': 0})
            fixed_count += 1
    
    # Проверяем плейлисты
    if 'playlists' in data:
        for i, playlist in enumerate(data['playlists']):
            if isinstance(playlist, dict):
                if 'id' not in playlist:
                    playlist['id'] = f"playlist_{i}"
                    fixed_count += 1
    
    # Проверяем настроения
    if 'moods' in data:
        for i, mood in enumerate(data['moods']):
            if isinstance(mood, dict):
                if 'id' not in mood:
                    mood['id'] = f"mood_{i}"
                    fixed_count += 1
    
    return {
        'status': 'ok', 
        'message': f'Исправлено {fixed_count} проблем', 
        'data': data
    }

# Пример использования
test_data = {
    "tracks": [
        {"name": "Song One", "duration": 200},
        "Bad Track Name",
        {},
        {"id": "1", "name": "", "duration": 300}
    ],
    "playlists": [{}],
    "moods": [{"id": "happy"}, {}]
}

result = verify_integrity_and_fix(test_data)
print(result['message'])
