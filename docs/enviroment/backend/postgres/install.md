# Установка PostgreSQL
## Windows
* Скачайте PostgreSQL с [официального сайта](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
* Запустите установщик. Выберите PostgreSQL-сервер и консольную утилиту psql
## Debian
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
## Arch
* Установите PostgreSQL
```
sudo pacman -Sy postgresql
```
* Инициализируйте кластер базы данных
```
sudo su postgres -l
initdb --locale $LANG -E UTF8 -D '/var/lib/postgres/data/'
exit
```
* Запустите сервер PostgreSQL и добавьте его запуск в автозагрузку
```
sudo systemctl start postgresql
sudo systemctl enable postgresql
```