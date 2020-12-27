# Установка PostGIS
## Arch
```
sudo pacman -Suy postgis
```

# Включение расширения
* Подключитесь к своей БД
* Включите расширения
```
CREATE EXTENSION postgis;
```