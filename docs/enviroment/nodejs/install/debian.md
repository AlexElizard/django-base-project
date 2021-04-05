* Скачайте скрипт установки предпочитаемой версии :
```
cd ~ && mkdir -p nodejs && cd nodejs && curl -sL https://deb.nodesource.com/setup_15.x -o nodesource_setup.sh
```
* Запустите скрипт:
```
sudo bash nodesource_setup.sh && cd ~ && rm -rf ./nodejs
```
* Установите Node.js:
```
sudo apt update && sudo apt install nodejs
```
* Верните пользователю права на каталог npm
```
sudo chown -R $(whoami) ~/.npm
```