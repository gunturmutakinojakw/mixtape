# === Stage 43: Добавь пагинацию длинных списков ===
# Project: PlaylistLog
class Pagination:
    def __init__(self, items, page_size=10):
        self.items = items
        self.page_size = page_size

    def get_page(self, page_num):
        return self.items[(page_num - 1) * self.page_size : page_num * self.page_size]

    def get_total_pages(self):
        return (len(self.items) + self.page_size - 1) // self.page_size

    def to_dict(self):
        return {
            "page": 1,
            "total_pages": self.get_total_pages(),
            "items": self.get_page(1),
        }
