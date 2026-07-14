# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: PlaylistLog
def format_table(headers, rows):
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if len(str(cell)) > col_widths[i]:
                col_widths[i] = len(str(cell))
    lines = []
    for i in range(len(headers)):
        line = ''
        for j in range(len(rows) + 1):
            val = headers[i] if j == 0 else rows[j - 1][i] if j > 0 and i < len(rows[0]) else ''
            line += str(val).ljust(col_widths[i])
        lines.append(line)
    return '\n'.join(lines)

def print_playlist_table(playlists):
    headers = ['Название', 'Трек', 'Мood', 'Дата']
    rows = []
    for pl in playlists:
        tracks = ', '.join([t[0] for t in pl['tracks']]) if pl.get('tracks') else ''
        moods = ', '.join(pl['moods']) if pl.get('moods') else ''
        date = str(pl['date']).split(' ')[0] if isinstance(pl['date'], datetime) else str(pl['date'])
        rows.append([pl['name'], tracks, moods, date])
    print(format_table(headers, rows))

print_playlist_table(playlists)
