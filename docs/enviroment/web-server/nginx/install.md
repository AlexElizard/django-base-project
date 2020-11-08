# Установка Nginx

## Debian
* Подключите apt-репозиторий
```
echo "deb http://nginx.org/packages/debian `lsb_release -cs` nginx" | sudo tee /etc/apt/sources.list.d/nginx.list
```
* Скачайте ключ проверки для apt
```
curl -fsSL https://nginx.org/keys/nginx_signing.key | sudo apt-key add -
```
* Установите nginx
```
sudo apt update && sudo apt install nginx
```