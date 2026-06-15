# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: PlaylistLog
def edit_entry(entry_id, updates):
    if entry_id not in entries:
        print(f"Запись с ID {entry_id} не найдена.")
        return False
    for key, value in updates.items():
        if key in entry_fields and value is not None:
            entries[entry_id][key] = value
    print(f"Запись #{entry_id} обновлена успешно.")
    return True
