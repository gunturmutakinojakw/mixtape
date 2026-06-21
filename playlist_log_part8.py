# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: PlaylistLog
def main():
    import sys, json, os
    DATA_FILE = "playlist_log.json"
    def load_data(): return json.load(open(DATA_FILE)) if os.path.exists(DATA_FILE) else {"playlists": {}, "history": [], "moods": {}}
    def save_data(data): open(DATA_FILE, "w").write(json.dumps(data, ensure_ascii=False, indent=2))
    data = load_data()
    print("\n=== PlaylistLog ===")
    while True:
        cmd = input("1. Создать плейлист 2. Добавить трек 3. Изменить настроение 4. История прослушивания 5. Выход\n> ").strip()
        if not cmd: continue
        try:
            choice, *args = map(int, cmd.split())
        except ValueError: continue
        if choice == 1 and args:
            name = input("Название плейлиста: ")
            data["playlists"][name] = {"tracks": [], "moods": []}
            print(f"Плейлист '{name}' создан.")
        elif choice == 2 and args:
            playlist_name, track_title, artist = [input(x) for x in ["Плейлист:", "Название трека:", "Исполнитель:"]]
            if playlist_name not in data["playlists"]: print("Ошибка: плейлист не найден."); continue
            mood = input("Настроение (например, happy): ") or "neutral"
            track_id = f"{playlist_name}_{track_title}"
            data["history"].append({"id": len(data["history"]) + 1, "track": track_title, "artist": artist, "playlist": playlist_name, "mood": mood})
            data["playlists"][playlist_name]["tracks"].append(track_id)
            if mood not in data["playlists"][playlist_name]["moods"]: data["playlists"][playlist_name]["moods"].append(mood)
            print(f"Трек '{track_title}' добавлен.")
        elif choice == 3 and args:
            playlist_name, track_idx = [input(x) for x in ["Плейлист:", "Индекс трека (0-based):"]]
            if playlist_name not in data["playlists"]: print("Ошибка: плейлист не найден."); continue
            try: moods = input("Новые настроения через запятую: ").split(",")
            except: pass
            for mood in moods: data["playlists"][playlist_name]["moods"].append(mood.strip())
            print(f"Настроения обновлены.")
        elif choice == 4 and args:
            limit = int(input("Количество записей в истории (по умолчанию 10): ") or "10")
            for rec in reversed(data["history"][-limit:]): print(f"{rec['id']}. {rec['track']} by {rec['artist']} ({rec['playlist']}) - {rec['mood']}")
        elif choice == 5: break
        else: print("Неверный выбор.")
    save_data(data)
