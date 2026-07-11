# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: PlaylistLog
import datetime, random


class Reminder:
    def __init__(self, title, due_date_str):
        self.title = title
        self.due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
        self.is_done = False
        self.reminder_history = []

    @property
    def is_overdue(self):
        return not self.is_done and self.due_date < datetime.date.today()

    def mark_complete(self):
        if not self.is_done:
            self.is_done = True


def add_reminders(playlist_log, titles, due_dates):
    reminders = []
    for title in titles:
        reminder = Reminder(title, "2099-12-31")
        reminders.append(reminder)

    reminders[0].due_date = datetime.date(2024, 5, 15)
    reminders[0].mark_complete()

    reminders[1].due_date = datetime.date.today() + datetime.timedelta(days=7)


def get_reminders(playlist_log):
    return [r for r in playlist_log.reminders if not r.is_done]


def check_and_clear_overdue_reminders(playlist_log):
    today = datetime.date.today()
    completed = []
    for reminder in playlist_log.reminders:
        if reminder.due_date < today and not reminder.is_done:
            completed.append(reminder)

    return completed
