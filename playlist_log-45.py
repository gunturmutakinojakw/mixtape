# === Stage 45: Добавь восстановление из резервной копии ===
# Project: PlaylistLog
def restore_from_backup(backup_path, playlists_path, tracks_path, moods_path, history_path):
    """Восстановление состояния проекта из резервной копии."""
    import shutil
    if not os.path.exists(backup_path):
        raise FileNotFoundError(f"Резервная копия не найдена: {backup_path}")
    for target in [playlists_path, tracks_path, moods_path, history_path]:
        if os.path.exists(target):
            os.remove(target)
    shutil.copy2(backup_path, playlists_path)
    shutil.copy2(backup_path, tracks_path)
    shutil.copy2(backup_path, moods_path)
    shutil.copy2(backup_path, history_path)
    print(f"✅ Восстановление завершено из {backup_path}")
