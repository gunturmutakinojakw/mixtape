# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: PlaylistLog
def export_report(playlist_log):
    """Export a compact text report of the playlist log."""
    lines = []
    lines.append("=== PlaylistLog Report ===")
    lines.append(f"Date: {playlist_log['date']}")
    lines.append(f"Total tracks: {playlist_log['total_tracks']}")
    lines.append(f"Total minutes: {playlist_log['total_minutes']} min")

    if playlist_log['mood_counts']:
        lines.append("Moods:")
        for mood, count in sorted(playlist_log['mood_counts'].items(), key=lambda x: -x[1]):
            lines.append(f"  {mood}: {count}")

    if playlist_log['top_artists']:
        lines.append("Top artists:")
        for artist, count in playlist_log['top_artists'].items():
            lines.append(f"  {artist}: {count}")

    lines.append("=== End ===")
    return "\n".join(lines)
