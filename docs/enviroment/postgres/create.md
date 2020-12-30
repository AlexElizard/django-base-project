* Подключитесь к PostgreSQL:
```
# Windows
Пуск -> Все программы -> Postgres -> SQL Shell

# Linux
sudo su postgres
psql
```
* Создайте пользователя, базу данных и дайте пользователю права на эту базу данных:
```
CREATE USER dbuser PASSWORD 'password';
CREATE DATABASE dbname;
GRANT ALL PRIVILEGES ON DATABASE dbname TO dbuser;
```
