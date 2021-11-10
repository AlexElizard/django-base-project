import uuid


def is_valid_uuid(value: str, version: int = 4) -> bool:
    """Проверяет является ли value валидным uuid"""
    try:
        uuid.UUID(value, version=version)
    except ValueError:
        return False
    else:
        return True


def progress_bar(current, total, title="Please wait", bar_len=50):
    """Прогресс бар для терминала"""
    percent_done = round(100 * (current + 1) / total, 1)
    done_str = "#" * int(bar_len * percent_done / 100)
    space_str = "-" * (bar_len - len(done_str))
    print(f"⏳ {title}: [{done_str}{space_str}] {percent_done}% done", end='\r')
    if round(percent_done) == 100:
        print('✅ ')


def lorem_image_url(width: int, height: int):
    """Генератор ссылки на случайное изображение"""
    return f"https://loremflickr.com/{width}/{height}?lock={uuid.uuid4()}"
