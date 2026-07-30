# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: PlaylistLog
def undo_last_action(self):
    """Откатывает последнее действие: добавление трека, плейлиста или запись прослушивания."""
    if not self._undo_stack:
        print("Нет действий для отката.")
        return
    
    action = self._undo_stack.pop()
    
    if action[0] == 'track_added':
        playlist_name, track_info = action[1], action[2]
        for i, t in enumerate(self.playlists[playlist_name].tracks):
            if t.title == track_info['title'] and t.artist == track_info.get('artist', ''):
                self.playlists[playlist_name].tracks.pop(i)
                break
    
    elif action[0] == 'playlist_added':
        playlist_name = action[1]
        del self.playlists[playlist_name]
    
    elif action[0] == 'listening_recorded':
        track_title, artist, duration = action[1], action[2], action[3]
        for i, rec in enumerate(self.history):
            if rec['track'] == track_title and rec.get('artist', '') == artist:
                self.history.pop(i)
                break
    
    elif action[0] == 'mood_added':
        mood = action[1]
        for playlist_name, p in self.playlists.items():
            if any(m['name'] == mood['name'] and m.get('color', '') == mood.get('color', '') 
                   for m in p.moods):
                new_mood = {k: v for k, v in mood.items() if k != 'count'}
                del new_mood['count']
                self.playlists[playlist_name].moods.append(new_mood)
    
    elif action[0] == 'track_removed':
        playlist_name, track_info = action[1], action[2]
        for i, t in enumerate(self.playlists[playlist_name].tracks):
            if t.title == track_info['title'] and t.artist == track_info.get('artist', ''):
                self.playlists[playlist_name].tracks.pop(i)
                break
    
    print(f"Отменено действие: {action[0]}")
