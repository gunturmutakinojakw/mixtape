# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: PlaylistLog
def get_next_action(state, actions):
    if not state['history']:
        return "Начни добавлять треки в плейлист"
    
    last_tracks = [t for t in state['tracks'] if t.get('added_date')]
    if not last_tracks:
        return "Добавь первый трек, чтобы начать журнал"
    
    recent_track = max(last_tracks, key=lambda x: x['added_date'])
    moods = set(t['mood'] for t in state['tracks'] if t.get('mood'))
    
    if not moods:
        return "Укажи настроение для добавленных треков"
    
    avg_mood_score = sum(mood_scores.get(m, 5) for m in moods) / len(moods)
    
    if avg_mood_score > 3.5 and recent_track['duration'] < 180:
        return f"Слушай больше треков длительностью {recent_track['duration']}+ минут для глубокого погружения"
    elif avg_mood_score < 2.5:
        return "Попробуй добавить трек с более позитивным настроением"
    
    if recent_track.get('genre') and genre_popularity.get(recent_track['genre'], 0) > 3:
        return f"Продолжай слушать {recent_track['genre']}-музыку, она популярна в журнале"
    
    return "Добавь трек с новым жанром для разнообразия журнала"
