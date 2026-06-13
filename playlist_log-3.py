# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: PlaylistLog
class PlaylistLog:
    def __init__(self):
        self._tracks = []
        self._playlists = {}
        self._moods = set()
        self._history = []

    def add_track(self, title, artist, mood=None):
        track_id = len(self._tracks) + 1
        record = {"id": track_id, "title": title, "artist": artist, "mood": mood}
        if mood:
            self._moods.add(mood)
        self._history.append(record.copy())
        return record

    def add_playlist(self, name):
        playlist_id = len(self._playlists) + 1
        self._playlists[name] = {"id": playlist_id, "tracks": []}
        return self._playlists[name]
