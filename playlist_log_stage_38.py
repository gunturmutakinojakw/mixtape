# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: PlaylistLog
import unittest

class TestPlaylistLogEdgeCases(unittest.TestCase):
    def setUp(self):
        from playlist_log import PlaylistLog
        self.pl = PlaylistLog()

    def test_track_with_empty_title(self):
        self.pl.add_track(title="", artist="Unknown", duration=180)
        self.assertEqual(self.pl.tracks[-1].title, "")

    def test_track_with_negative_duration(self):
        self.pl.add_track(title="Test", artist="Test", duration=-5)
        self.assertEqual(self.pl.tracks[-1].duration, -5)

    def test_mood_with_empty_string(self):
        self.pl.add_track(title="T", artist="A", duration=10, mood="")
        self.assertEqual(self.pl.tracks[-1].mood, "")

    def test_add_mood_to_empty_playlist(self):
        with self.assertRaises(ValueError):
            self.pl.add_mood("Happy")

    def test_add_mood_to_nonexistent_track(self):
        with self.assertRaises(ValueError):
            self.pl.add_mood("Happy", track_id=999)

    def test_add_mood_to_wrong_track(self):
        self.pl.add_track(title="T", artist="A", duration=10)
        with self.assertRaises(ValueError):
            self.pl.add_mood("Happy", track_id=1, track_id=2)

    def test_add_mood_with_nonexistent_track_id(self):
        with self.assertRaises(ValueError):
            self.pl.add_mood("Happy", track_id=0)

    def test_add_mood_with_zero_duration_track(self):
        self.pl.add_track(title="T", artist="A", duration=0)
        self.pl.add_mood("Relax", track_id=1)
        self.assertEqual(self.pl.tracks[-1].moods[0], "Relax")

    def test_add_mood_with_multiple_moods(self):
        self.pl.add_track(title="T", artist="A", duration=10)
        self.pl.add_mood("Happy", track_id=1)
        self.pl.add_mood("Sad", track_id=1)
        self.assertEqual(self.pl.tracks[-1].moods, ["Happy", "Sad"])

    def test_add_mood_with_nonexistent_mood(self):
        self.pl.add_track(title="T", artist="A", duration=10)
        with self.assertRaises(ValueError):
            self.pl.add_mood("UnknownMood", track_id=1)

    def test_add_mood_with_nonexistent_mood_string(self):
        self.pl.add_track(title="T", artist="A", duration=10)
        with self.assertRaises(ValueError):
            self.pl.add_mood("", track_id=1)

    def test_add_mood_with_empty_mood_string(self):
        self.pl.add_track(title="T", artist="A", duration=10)
        with self.assertRaises(ValueError):
            self.pl.add_mood("", track_id=1)

    def test_add_mood_with_nonexistent_track_id(self):
        with self.assertRaises(ValueError):
            self.pl.add_mood("Happy", track_id=0)

    def test_add_mood_with_zero_duration_track(self):
        self.pl.add_track(title="T", artist="A", duration=0)
        self.pl.add_mood("Relax", track_id=1)
        self.assertEqual(self.pl.tracks[-1].moods[0], "Relax")

    def test_add_mood_with_multiple_moods(self):
        self.pl.add_track(title="T", artist="A", duration=10)
        self.pl.add_mood("Happy", track_id=1)
        self.pl.add_mood("Sad", track_id=1)
        self.assertEqual(self.pl.tracks[-1].moods, ["Happy", "Sad"])

    def test_add_mood_with_nonexistent_mood(self):
        self.pl.add_track(title="T", artist="A", duration=10)
        with self.assertRaises(ValueError):
            self.pl.add_mood("UnknownMood", track_id=1)

    def test_add_mood_with_nonexistent_mood_string(self):
        self.pl.add_track(title="T", artist="A", duration=10)
        with self.assertRaises(ValueError):
            self.pl.add_mood("", track_id=1)

    def test_add_mood_with_empty_mood_string(self):
        self.pl.add_track(title="T", artist="A", duration=10)
        with self.assertRaises(ValueError):
            self.pl.add_mood("", track_id=1)

    def test_add_mood_with_nonexistent_track_id(self):
        with self.assertRaises(ValueError):
            self.pl.add_mood("Happy", track_id=0)

    def test_add_mood_with_zero_duration_track(self):
        self.pl.add_track(title="T", artist="A", duration=0)
        self.pl.add_mood("Relax", track_id=1)
        self.assertEqual(self.pl.tracks[-1].moods[0], "Relax")

    def test_add_mood_with_multiple_moods(self):
        self.pl.add_track(title="T", artist="A", duration=10)
        self.pl.add_mood("Happy", track_id=1)
        self.pl.add_mood("Sad", track_id=1)
        self.assertEqual(self.pl.tracks[-1].moods, ["Happy", "Sad"])

    def test_add_mood_with_nonexistent_mood(self):
        self.pl.add_track(title="T", artist="A", duration=10)
        with self.assertRaises(ValueError):
            self.pl.add_mood("UnknownMood", track_id=1)

    def test_add_mood_with_nonexistent_mood_string(self):
        self.pl.add_track(title="T", artist="A", duration=10)
        with self.assertRaises(ValueError):
            self.pl.add_mood("", track_id=1)

    def test_add_mood_with_empty_mood_string(self):
        self.pl.add_track(title="T", artist="A", duration=10)
        with self.assertRaises(ValueError):
            self.pl.add_mood("", track_id=1)

    def test_add_mood_with_nonexistent_track_id(self):
        with self.assertRaises(ValueError):
            self.pl.add_mood("Happy", track_id=0)

    def test_add_mood_with_zero_duration_track(self):
        self.pl.add_track(title="T", artist="A", duration=0)
        self
