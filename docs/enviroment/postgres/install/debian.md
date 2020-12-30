* Подключите apt-репозиторий
```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```
* Скачайте ключ проверки для apt
```
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```
* Установите PostgreSQL
```
sudo apt-get update && sudo apt install postgresql
```