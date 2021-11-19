### Установка и настройка PyCharm для бекендеров
* Скачайте и установите **Professional** версию с [официального сайта](https://www.jetbrains.com/pycharm/download/#section=windows)
* Создание pipenv окружения<br>
    * Перейдите в ***Settings -> Project -> Project Interpreter***. 
    * Клик по ***"гайке" -> Add -> Pipenv Environment***.
    * Отключаем флаг ***Install packages from Pipfile***.
* Включаем поддержку Django:
    * Перейдите в ***Settings -> Languages & Frameworks -> Django***.
    * Включите ***Enable Django Support***.
    * В ***Setting*** укажите ***config/settings.py***, а ***Manage script*** укажите ***manage.py***
* Настройка Code Style:
    * Перейдите в ***Settings -> Editor -> Code Style***. 
    * Установите ***Hard wrap at*** равным 99
* Создание Django-server:
    * Перейдите в ***Run/Debug Configuration***. 
    * Клик по ***+ -> Django Server***. 
 