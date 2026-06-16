# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: PlaylistLog
def delete_playlist(playlist_id):
    if playlist_id in playlists:
        del playlists[playlist_id]
        return True
    raise ValueError(f"Плейлист {playlist_id} не найден")

def delete_track(track_id, playlist_name=None):
    for pid, pl in list(playlists.items()):
        if track_id in pl['tracks']:
            if playlist_name and pid != playlist_name:
                continue
            del pl['tracks'][track_id]
            return True
    raise ValueError(f"Трек {track_id} не найден")

def delete_mood(mood_id, playlist_name=None):
    for pid, pl in list(playlists.items()):
        if mood_id in pl['moods']:
            if playlist_name and pid != playlist_name:
                continue
            del pl['moods'][mood_id]
            return True
    raise ValueError(f"Настроение {mood_id} не найдено")

def delete_history_entry(entry_id):
    if entry_id in history_entries:
        del history_entries[entry_id]
        return True
    raise ValueError(f"Запись истории {entry_id} не найдена")
