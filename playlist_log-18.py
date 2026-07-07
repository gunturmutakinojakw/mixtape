# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: PlaylistLog
class Tag:
    def __init__(self, name):
        self.name = str(name).lower().strip()

    @property
    def is_valid(self):
        return len(self.name) > 0 and len(self.name) <= 50

    def __repr__(self):
        return f"Tag('{self.name}')"


class Playlist:
    def add_tag(self, tag_name):
        if not self.tags.is_valid:
            raise ValueError(f"Invalid tag name: {tag_name}")
        tag = Tag(tag_name)
        if tag.name in [t.name for t in self.tags]:
            return
        self.tags.add(tag)

    def remove_tag(self, tag_name):
        tag = Tag(tag_name)
        self.tags = [t for t in self.tags if t.name != tag.name]


class Track:
    def add_tag(self, tag_name):
        if not self.tags.is_valid:
            raise ValueError(f"Invalid tag name: {tag_name}")
        tag = Tag(tag_name)
        if tag.name in [t.name for t in self.tags]:
            return
        self.tags.add(tag)

    def remove_tag(self, tag_name):
        tag = Tag(tag_name)
        self.tags = [t for t in self.tags if t.name != tag.name]


class Mood:
    def __init__(self, name, color=None):
        self.name = str(name).lower().strip()
        self.color = color

    @property
    def is_valid(self):
        return len(self.name) > 0 and len(self.name) <= 50


class HistoryEntry:
    def __init__(self, track, timestamp=None):
        self.track = track
        self.timestamp = timestamp or datetime.now()
