# Установка Python и pipenv
## Windows
* Скачайте установщик с [официального сайта](https://www.python.org/downloads/)
* Запустите установщик и поставьте галочку напротив ***Add Python to PATH***
* Нажмите ***Install Now***
* Устанавливаем ***pipenv***:
```
pip install pipenv
```

## Debian
* Обновите список пакетов:
```
sudo apt update
```
* Устанавливаем библиотеки для компиляции
```
sudo apt install build-essential checkinstall
sudo apt install python3-tk libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev
sudo apt install libpq-dev python3-dev
```
* Скачиваем и распаковываем иходники:
```
cd ~ && mkdir python && cd python
sudo wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz
sudo tar xzf Python-3.8.3.tgz
```
* Собираем и компилируем
```
cd Python-3.8.3
sudo ./configure --enable-optimizations
sudo make altinstall
```
* Устанавливаем ***pipenv***:
```
sudo pip3.8 install pipenv
```