# Базовый проект и документация
* [Список пакетов](docs/packages.md), участвующих в сборке
* [Google Maps](docs/other/google.md)
* [Настройки PyCharm](docs/ide/pycharm.md)

# Сборка проекта
* [Установка рабочего окружения](https://github.com/AlexElizard/env-doc)
* [Запустите проект](docs/apps/django/production.md)
* [Соберите frontend](docs/apps/react/production.md)

# Полезные функции
```python
def progress_bar(current, total, title="Please wait", bar_len=50):
    percent_done = round(100 * (current + 1) / total, 1)
    done_str = "#" * int(bar_len * percent_done / 100)
    space_str = "-" * (bar_len - len(done_str))
    print(f"⏳ {title}: [{done_str}{space_str}] {percent_done}% done", end='\r')
    if round(percent_done) == 100:
        print('✅ ')


def lorem_image_url(width: int, height: int):
    return f"https://loremflickr.com/{width}/{height}?lock={uuid.uuid4()}"
```
