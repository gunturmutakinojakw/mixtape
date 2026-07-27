# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: PlaylistLog
def switch_profile():
    """Переключение активного профиля: выбор, сохранение и обновление UI."""
    from datetime import datetime
    
    # --- 1. Выбор профиля (появляется только если есть несколько) ---
    profiles = list(profiles_data.keys())
    if len(profiles) <= 1:
        return None
    
    def show_switch_dialog():
        """Окно выбора профиля (диалог)."""
        nonlocal current_profile
        
        # Получаем список доступных профилей и отображаем их в диалоге
        dialog = Dialog("Выберите профиль:", profiles)
        
        if dialog.show() is None:  # Пользователь отменил выбор
            return None
        
        new_profile = dialog.selected_value
        
        # Проверяем, что выбранный профиль существует и не выбран
        if not new_profile or new_profile == current_profile:
            return None
        
        # Сохраняем выбор в глобальную переменную
        global active_profile
        active_profile = new_profile
        current_profile = new_profile
        
        # Обновляем данные профиля
        profile_data = profiles_data[new_profile]
        if current_profile not in profile_data:
            return None  # Профиль не существует
        
        # Обновляем UI для отображения нового профиля
        update_profile_ui(new_profile)
        
        # Показываем уведомление о успешном переключении
        show_notification(f"Переключение на профиль {new_profile} завершено.", "info")
