# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: PlaylistLog
def demo_commands():
    """Демо-команды для ручного тестирования."""
    commands = {
        "create_mood": lambda: create_mood("happy"),
        "add_track": lambda: add_track_to_playlist("demo", "Artist - Song Title", "https://example.com/song1.mp3", "2024-01-15T10:00:00Z"),
        "create_playlist": lambda: create_playlist("Demo Playlist"),
        "add_mood": lambda: add_mood_to_track("demo", "happy"),
        "save_log": lambda: save_log(),
    }

    while True:
        try:
            cmd = input("\nPlaylistLog Demo > ").strip().lower()
            if cmd in commands:
                result = commands[cmd]()
                print(result)
            elif cmd == "exit":
                break
            else:
                print(f"Unknown command: {cmd}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    demo_commands()
