# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: PlaylistLog
# PlaylistLog — метрики проекта (этап 28)
def project_metrics():
    """Компактный блок для подсчёта ключевых метрик."""
    import os, json
    root = os.path.dirname(os.path.abspath(__file__))
    files = sorted([f for f in os.listdir(root) if f.endswith(('.py', '.json', '.txt'))])
    total_lines = sum(sum(1 for _ in open(os.path.join(root, f))) for f in files)
    py_files = [f for f in files if f.endswith('.py')]
    data_files = [f for f in files if f.endswith(('.json', '.txt'))]
    metrics = {
        "total_python_files": len(py_files),
        "total_data_files": len(data_files),
        "total_lines_of_code": total_lines,
        "project_root": root,
        "file_list": files[:10],  # топ-10 файлов для примера
    }
    return metrics

# Пример использования:
# print(project_metrics())
