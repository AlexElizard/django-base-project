# Установка PostGIS
## Arch
```
sudo pacman -Sy postgis
```

# Включение расширения
* Подключитесь к своей БД
* Включите расширения
```
CREATE EXTENSION postgis;
```