# Запуск проекта
* Склонируйте проект и перейдите в ветку develop или обновите эту ветку
* Установите зависимости
```
pipenv sync --dev
```
* Создайте ***.env*** файл на основе файла ***.env.example*** в корневой папке проекта
* Перейдите в виртуальное окружение. <br>
  ПРИМЕЧАНИЕ: Если у вас будет ошибка ***UnicodeDecodeError: 'charmap'***, то уберите в ***.env***-файле кириллицу:
```
pipenv shell
```
* Загрузите миграции:
```
python manage.py migrate
```
* Загрузите фикстуры. <br>
  ПРИМЕЧАНИЕ: Если у вас ошибка ***CommandError: No fixture named 'init' found***, то пропустите этот шаг:
```
python manage.py loaddata init
python manage.py loaddata test
```
* Запустите сервер разработчика:
```
python manage.py runserver
```

