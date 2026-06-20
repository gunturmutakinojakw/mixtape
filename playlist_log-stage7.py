# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: PlaylistLog
def sort_entries(criteria='date'):
    if criteria == 'date':
        return sorted(entries, key=lambda x: x['timestamp'], reverse=True)
    elif criteria == 'priority':
        return sorted(entries, key=lambda x: -x.get('priority', 0))
    elif criteria == 'name':
        return sorted(entries, key=lambda x: x['track_name'].lower())
    else:
        raise ValueError(f"Неизвестный критерий сортировки: {criteria}")
