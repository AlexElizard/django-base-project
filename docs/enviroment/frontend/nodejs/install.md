## Установка Node.js

## Debian
* Обновите список пакетов:
```
sudo apt update
```
* Скачайте скрипт установки предпочитаемой версии :
```
cd ~ && mkdir nodejs && cd nodejs
curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh
```
* Запустите скрипт:
```
sudo bash nodesource_setup.sh
```
* Установите Node.js:
```
sudo apt install nodejs
```