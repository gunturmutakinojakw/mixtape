# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: PlaylistLog
import unittest


class TestPlaylistLog(unittest.TestCase):
    def test_add_track(self):
        pl = PlaylistLog()
        pl.add_track("Radiohead", "Karma Police", "Alternative", "Sad", 180)
        self.assertEqual(len(pl.tracks), 1)
        self.assertEqual(pl.tracks[0].title, "Karma Police")
        self.assertEqual(pl.tracks[0].duration, 180)

    def test_add_playlist(self):
        pl = PlaylistLog()
        pl.add_track("Radiohead", "Karma Police", "Alternative", "Sad", 180)
        pl.add_track("Radiohead", "Creep", "Alternative", "Sad", 200)
        pl.add_playlist("Sad Vibes", [pl.tracks[0], pl.tracks[1]])
        self.assertEqual(len(pl.playlists), 1)
        self.assertEqual(pl.playlists[0].name, "Sad Vibes")
        self.assertEqual(len(pl.playlists[0].tracks), 2)

    def test_listening_history(self):
        pl = PlaylistLog()
        pl.add_track("Radiohead", "Karma Police", "Alternative", "Sad", 180)
        pl.add_track("Radiohead", "Creep", "Alternative", "Sad", 200)
        pl.add_track("Radiohead", "High and Dry", "Alternative", "Sad", 240)
        pl.add_to_history("Karma Police")
        pl.add_to_history("Creep")
        pl.add_to_history("High and Dry")
        pl.add_to_history("Karma Police")
        self.assertEqual(pl.history, ["Karma Police", "Creep", "High and Dry", "Karma Police"])

    def test_mood_stats(self):
        pl = PlaylistLog()
        pl.add_track("Radiohead", "Karma Police", "Alternative", "Sad", 180)
        pl.add_track("The Beatles", "Yesterday", "Rock", "Sad", 125)
        pl.add_track("Pink Floyd", "Comfortably Numb", "Rock", "Depressed", 384)
        pl.add_mood_stats("Sad")
        self.assertEqual(pl.mood_stats["Sad"], 2)
        self.assertEqual(pl.mood_stats["Depressed"], 1)


if __name__ == "__main__":
    unittest.main()
