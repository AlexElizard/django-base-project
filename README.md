# Базовый проект и документация
* [Список пакетов](docs/packages.md), участвующих в сборке 

## Запуск проекта в режиме разработчика
* [Windows](docs/develop/windows.md)
* [Arch Linux](docs/develop/arch.md)

## Запуск проекта в режиме production
* [Debian](docs/production/debian.md)

## Полезные функции
```python
def progress_bar(current, total, title="Please wait", bar_len=50):
    percent_done = round(100 * (current + 1) / total, 1)
    done_str = "#" * int(bar_len * percent_done / 100)
    space_str = "-" * (bar_len - len(done_str))
    print(f"⏳ {title}: [{done_str}{space_str}] {percent_done}% done", end='\r')
    if round(percent_done) == 100:
        print('✅ ')
```