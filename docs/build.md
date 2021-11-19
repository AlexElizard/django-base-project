# Сборка Проекта
## Сборка django-base-project
* Склонируйте проект и перейдите в нужную ветку
* Создайте ***.env*** файл на основе файла ***.env.example*** в корневой папке проекта <br>
  ПРИМЕЧАНИЕ: Сгенерировать **`SECRET KEY`** можно [здесь](https://djecrety.ir/)
* Перейдите в виртуальное окружение. <br>
  ПРИМЕЧАНИЕ: Если у вас будет ошибка ***UnicodeDecodeError: 'charmap'***, то уберите в ***.env***-файле кириллицу:
```
pipenv shell
```
## Develop
* Соберите проект
```
make dev-build
```
## Production
* Соберите проект
```
make build
```
* Создайте файлы сокета и сервиса Gunicorn и следуйте инструкциям скрипта
```
sudo python config/gunicorn.py
```
### Сборка React-проекта
* Перейдите в папку frontend-проекта
* Установите зависимости: 
```
npm install --only=production
```
* Запустите сборку проекта
```
npm run-script build
```
### Настройка Nginx
* Создайте [файл-конфигурации nginx](https://github.com/AlexElizard/env-doc/blob/master/docs/web_servers/nginx/nginx.md#%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B3%D1%83%D1%80%D0%B0%D1%86%D0%B8%D1%8F)
* Перезапустите nginx
```sudo service nginx restart```