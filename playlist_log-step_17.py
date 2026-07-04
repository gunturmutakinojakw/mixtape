# === Stage 17: Добавь группировку записей по категориям ===
# Project: PlaylistLog
from collections import defaultdict, Counter

def group_by_category(records):
    grouped = defaultdict(list)
    for record in records:
        category = record.get('category', 'other')
        grouped[category].append(record)
    
    sorted_categories = sorted(grouped.keys(), key=lambda c: len(grouped[c]), reverse=True)
    return {cat: group_by_category(records)[cat] if cat in group_by_category(records) else [] for cat in sorted_categories}
