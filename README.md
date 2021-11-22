# Базовый проект и документация
* [Список пакетов](docs/packages.md), участвующих в сборке
* [Google Maps](docs/google.md)
* [Настройки PyCharm](docs/pycharm.md)

# Сборка проекта
* [Установка рабочего окружения](https://github.com/AlexElizard/env-doc)
* [Соберите проект](docs/build.md)

# Структура application
* application_name
  * admin - директория админ-панели приложения
    * __init__.py - файл для импорта админок из model_1/admin.py, model_2/admin.py, ...
    * model_1 - директория админки модели
      * admin.py - здесь хранится сама админка
      * filters.py - фильтры для админки
      * inlines.py - inline-блоки для админки
      * forms.py - формы для админки
    * model_2 - структура по аналогии с админкой model_1
  * fixtures
    * init.json - фикстура для инициализации на production сервера
    * test.json - фикстура, расширяющая init.json, для testing сервера
  * locale - директория для переводов
  * migrations - директория хранения миграций
  * models - директория моделей
    * __init__.py - файл для импорта моделей из model_1.py, model_2.py, ...
    * model_1.py - файл с описанием модели, queryset'ов, сигналов, которые слушает модель
    * model_2.py - по аналогии с model_1.py
  * rest
    * admin - API для кастомной админ-панели
        * model_1
          * filters - фильтры для данной модели
          * serializers - сериализаторы данной модели, сложные поля импортируются из сериализаторов соответствующих моделей
          * views - вьюшки для данной модели
        * model_2
        * urls.py - маршрутизатор
    * site - API для сайта. Структура по аналогии с admin
  * templates - директория для шаблонов
    * application_name
      