# Запуск проекта
* Склонируйте проект и перейдите в ветку develop или обновите эту ветку
* Установите зависимости
  * 
```
# Синхронизует пакеты с Pipfile.lock
pipenv sync --dev

# Устанавливает последние версии пакетов, игнорируя Pipfile.lock
pipenv install --dev
```
* Создайте ***.env*** файл на основе файла ***.env.example*** в корневой папке проекта <br>
  ПРИМЕЧАНИЕ: Сгенерировать **`SECRET KEY`** можно [здесь](https://djecrety.ir/)
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
```
python manage.py loaddata init
python manage.py loaddata test
```
* Запустите сервер разработчика:
```
python manage.py runserver
```

