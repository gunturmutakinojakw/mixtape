# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: PlaylistLog
def parse_date(date_str, fmt=None):
    """Parse a date string with fallback formats and return a datetime.date or None."""
    if not date_str:
        return None
    try:
        if fmt:
            return datetime.strptime(str(date_str), fmt).date()
        for f in ('%Y-%m-%d', '%d.%m.%Y', '%m/%d/%Y', '%Y/%m/%d'):
            d = date_str.strip().replace('.', '/').replace('-', '/')
            if d and len(d) == 10:
                try:
                    return datetime.strptime(d, f).date()
                except ValueError:
                    continue
        return None
    except Exception:
        return None
