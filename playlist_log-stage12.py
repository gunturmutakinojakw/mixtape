# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: PlaylistLog
def load_from_json(filepath):
    import json
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            print(f"Загружено {len(data)} записей из '{filepath}'")
            return data
        elif isinstance(data, dict):
            records = [data]
            print(f"Загружен 1 запись (объект) из '{filepath}'")
            return records
        else:
            raise ValueError("Неверный формат данных JSON")
    except FileNotFoundError:
        print(f"Файл не найден: {filepath}")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в '{filepath}': {e}")
        return []
