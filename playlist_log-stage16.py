# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: PlaylistLog
def calculate_monthly_stats(history):
    from collections import defaultdict
    stats = defaultdict(lambda: {'total': 0, 'minutes': 0})
    for entry in history:
        date_str = entry.get('date') or ''
        if not date_str: continue
        try: month_key = f"{date_str[:4]}-{date_str[5:7]}"
        except (IndexError, ValueError): continue
        stats[month_key]['total'] += 1
        duration = float(entry.get('duration_seconds') or 0)
        stats[month_key]['minutes'] += int(duration / 60) + (1 if duration % 60 else 0)
    return dict(sorted(stats.items()))
