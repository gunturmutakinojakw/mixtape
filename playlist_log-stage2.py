# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: PlaylistLog
class PlaylistLog:
    def __init__(self):
        self._playlists = {}
        self._history = []

    def validate_track(self, title: str, artist: str) -> bool:
        if not all(isinstance(x, str) and len(x.strip()) > 0 for x in [title, artist]):
            return False
        return True

    def add_playlist(self, name: str, tracks: list):
        if not self.validate_track(name, "") or not isinstance(tracks, list):
            print("Ошибка: невалидный плейлист")
            return False
        for t in tracks:
            if not self.validate_track(t["title"], t.get("artist", "")):
                print(f"Ошибка в треке: {t}")
                return False
        self._playlists[name] = {"tracks": tracks, "moods": []}
        return True

    def log_listen(self, playlist_name: str, track_index: int, mood: str):
        if not self.validate_track(playlist_name, "") or track_index < 0:
            print("Ошибка: невалидный вход")
            return False
        if playlist_name not in self._playlists:
            print(f"Плейлист {playlist_name} не найден")
            return False
        entry = {"playlist": playlist_name, "track_idx": track_index, "mood": mood}
        self._history.append(entry)
        self._playlists[playlist_name]["moods"].append(mood)
        return True

    def get_history(self):
        return self._history
