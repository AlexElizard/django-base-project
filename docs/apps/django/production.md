# Запуск проекта
* Склонируйте проект и перейдите в ветку develop или обновите эту ветку
* Установите зависимости
```
pipenv sync
```
* Создайте ***.env*** файл на основе файла ***.env.example*** в корневой папке проекта <br>
  ПРИМЕЧАНИЕ: Сгенерировать **`SECRET KEY`** можно [здесь](https://djecrety.ir/)
* Перейдите в виртуальное окружение. <br>
  ПРИМЕЧАНИЕ: Если у вас будет ошибка ***UnicodeDecodeError: 'charmap'***, то уберите в ***.env***-файле кириллицу:
```
pipenv shell
```
* Соберите файлы статики
```
pyhon manage.py collectstatic
```
* Загрузите миграции:
```
python manage.py migrate
```
* Загрузите фикстуры. <br>
```
python manage.py loaddata init
```
* Запустите wsgi-server. **workers = кол-во_ядер * 2 + 1**
```
gunicorn --workers=3 config.wsgi --reload -b 0.0.0.0:8000 --daemon
```
