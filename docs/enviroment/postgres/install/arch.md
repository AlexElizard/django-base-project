* Установите PostgreSQL
```
sudo pacman -Suy postgresql
```
* Инициализируйте кластер базы данных
```
sudo su postgres
initdb --locale $LANG -E UTF8 -D '/var/lib/postgres/data/'
exit
```
* Запустите сервер PostgreSQL и добавьте его запуск в автозагрузку
```
sudo systemctl start postgresql
sudo systemctl enable postgresql
```