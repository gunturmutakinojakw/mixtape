# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: PlaylistLog
import sys

def _is_tty():
    return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()

def _color_enabled():
    return _is_tty() and os.environ.get('PLAYLISTLOG_NO_COLOR') != '1'

def _reset():
    return '\033[0m'

def _bold():
    return '\033[1m'

def _dim():
    return '\033[2m'

def _yellow():
    return '\033[33m'

def _green():
    return '\033[32m'

def _red():
    return '\033[31m'

def _cyan():
    return '\033[36m'

def _magenta():
    return '\033[35m'

def _title(text):
    return f'{_bold()}{_cyan()}{text}{_reset()}'

def _subtitle(text):
    return f'{_bold()}{_dim()}{text}{_reset()}'

def _success(text):
    return f'{_green()}{text}{_reset()}'

def _error(text):
    return f'{_red()}{text}{_reset()}'

def _warning(text):
    return f'{_yellow()}{text}{_reset()}'

def _info(text):
    return f'{_cyan()}{text}{_reset()}'

def _prompt(text):
    return f'{_yellow()}{text}> {(_reset() if _color_enabled() else "")}'

def _status(label, text):
    return f'{_bold()}{label} {text}'

def _track_line(artist, title, duration, mood):
    return f'{_cyan()}{artist}{_reset()} - {_green()}{title}{_reset()} ({_dim()}{duration}{_reset()}) {_dim()}{mood}{_reset()}'

def _playlist_header(name, count):
    return f'{_bold()}{_yellow()}{name}{_reset()}: {_green()}{count} треков{_reset()}'

def _playlist_track(track):
    return _track_line(track['artist'], track['title'], track['duration'], track.get('mood', '—'))

def _history_entry(entry):
    return f'{_dim()}{entry["date"]}{_reset()} {_cyan()}{entry["mood"]}{_reset()} — {_green()}{entry["track"]}{_reset()}'

def _stats_section(label, data):
    return f'{_bold()}{_magenta()}{label}{_reset()}\n{_dim()}{_reset()}'.join(f'{_cyan()}{k}{_reset()}: {v}' for k, v in data.items())

def _progress_bar(current, total):
    pct = current / total
    filled = int(20 * pct)
    bar = '█' * filled + '░' * (20 - filled)
    return f'{_green()}{bar}{_reset()}'

def _separator():
    return _dim() + '─' * 50 + _reset()

def _clear_screen():
    print('\033[2J\033[H', end='')

def _print_banner():
    print(_clear_screen())
    print(_title('PlaylistLog'))
    print(_subtitle('Музыкальный журнал с плейлистами'))
    print()

def _confirm(question, default=True):
    prompt_text = _prompt(f'{question} [{_dim()}"y"{_reset()}]')
    print(prompt_text, end='')
    try:
        answer = input().strip().lower()
        if not answer:
            answer = 'y' if default else 'n'
        return answer in ('y', 'yes', '1', 'true')
    except (EOFError, KeyboardInterrupt):
        return default
