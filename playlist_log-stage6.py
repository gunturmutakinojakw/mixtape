# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: PlaylistLog
def filter_records(status=None, category=None, tags=None):
    filtered = []
    for record in all_playlists:
        if status and record.get('status') != status: continue
        if category and record.get('category') != category: continue
        if tags is None or set(record.get('tags', [])).intersection(tags):
            filtered.append(record)
    return filtered

def search_history(query=None, limit=10):
    results = []
    query_lower = query.lower() if query else ''
    for record in all_playlists:
        text = f"{record['title']} {record.get('mood', '')} {' '.join(record.get('tags', []))}".lower()
        if not query or query_lower in text: results.append(record)
        if len(results) >= limit: break
    return results
