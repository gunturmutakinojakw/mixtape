# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: PlaylistLog
import argparse
from playlistlog import app

def main():
    parser = argparse.ArgumentParser(description="PlaylistLog CLI")
    sub = parser.add_subparsers(dest="command")

    p_add_track = sub.add_parser("add-track", help="Добавить трек")
    p_add_track.add_argument("--playlist", "-p", help="ID плейлиста")
    p_add_track.add_argument("--title", "-t", help="Название трека")
    p_add_track.add_argument("--artist", "-a", help="Исполнитель")
    p_add_track.add_argument("--duration", "-d", type=int, help="Длительность (сек)")
    p_add_track.add_argument("--mood", "-m", help="Настроение")
    p_add_track.add_argument("--date", help="Дата прослушивания (YYYY-MM-DD)")

    p_add_playlist = sub.add_parser("add-playlist", help="Добавить плейлист")
    p_add_playlist.add_argument("--name", "-n", help="Название")
    p_add_playlist.add_argument("--genre", "-g", help="Жанр")
    p_add_playlist.add_argument("--mood", "-m", help="Настроение")
    p_add_playlist.add_argument("--date", help="Дата создания (YYYY-MM-DD)")

    p_list = sub.add_parser("list", help="Показать все")
    p_list.add_argument("--type", "-t", choices=["playlist", "track", "history"], help="Тип")

    p_history = sub.add_parser("history", help="История прослушивания")
    p_history.add_argument("--limit", "-l", type=int, default=10, help="Лимит")

    args = parser.parse_args()
    if hasattr(args, "command"):
        app.run(args)

if __name__ == "__main__":
    main()
