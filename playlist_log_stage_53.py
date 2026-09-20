# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: PlaylistLog
def load_playlist_from_text(path, separator=',', encoding='utf-8'):
    """Загружает плейлист из текстового файла в формате:
    название,трек1,трек2,...
    """
    with open(path, encoding=encoding) as f:
        line = f.readline().strip()
    parts = line.split(separator)
    name = parts[0]
    tracks = [t.strip() for t in parts[1:]]
    playlist = Playlist(name=name, tracks=tracks)
    return playlist
