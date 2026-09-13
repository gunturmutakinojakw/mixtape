# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: PlaylistLog
def self_check():
    print("=" * 60)
    print("PlaylistLog — самопроверка приложения")
    print("=" * 60)
    errors = []
    if not playlist_db:
        errors.append("playlist_db не инициализирован")
    for mood in mood_list:
        if not isinstance(mood, dict):
            errors.append(f"Некорректный mood: {mood}")
    if errors:
        print(f"⚠️  Найдено {len(errors)} проблем:")
        for e in errors:
            print(f"   - {e}")
    else:
        print("✅ Все проверки пройдены — приложение готово к работе!")
    print("=" * 60)

self_check()
