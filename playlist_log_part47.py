# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: PlaylistLog
def demo():
    """Показывает основной пользовательский сценарий PlaylistLog."""
    import random
    moods = ["happy", "sad", "energetic", "calm", "romantic", "angry"]
    artists = ["Radiohead", "Daft Punk", "Björk", "Tame Impala", "Portishead", "Massive Attack"]
    tracks = ["Creep", "Get Lucky", "Hyperballad", "Let It Happen", "Glory Box", "Boyz n the Hood"]
    playlists = {
        "Rainy Days": ["Rainy Drive", "Café Blues", "Stormy Night"],
        "Workout": ["Power Hour", "Running Man", "Gym Pump"],
        "Chill": ["Lo-Fi Beats", "Jazz Vibes", "Downtempo"],
        "Party": ["Dance Floor", "Club Mix", "Festival"],
    }
    history = []
    for _ in range(30):
        artist = random.choice(artists)
        track = random.choice(tracks)
        mood = random.choice(moods)
        length = random.randint(3, 8)
        history.append({"artist": artist, "track": track, "mood": mood, "length": length})
    print(f"🎵 PlaylistLog Demo — {len(history)} треков в истории:")
    for i, h in enumerate(history, 1):
        print(f"  {i:>2}. {h['artist']} — {h['track']} ({h['length']} мин) [{h['mood'].capitalize()}]")
    for name, tlist in playlists.items():
        print(f"\n📋 Плейлист: {name}")
        for t in tlist:
            print(f"   • {t}")
    print("\n✅ Demo завершен. PlaylistLog готов к использованию!")
