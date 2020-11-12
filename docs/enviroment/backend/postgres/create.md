# Создание пользователя БД
## Подключитесь к PostgreSQL:
* Windows
```
Пуск -> Все программы -> Postgres -> SQL Shell
```
* Debian или Arch
```
sudo -su postgres
psql
```
## Создание пользователя
* Создайте пользователя, базу данных и дайте пользователю права на эту базу данных:
```
CREATE USER dbuser PASSWORD 'password';
CREATE DATABASE dbname;
GRANT ALL PRIVILEGES ON DATABASE dbname TO dbuser;
```
