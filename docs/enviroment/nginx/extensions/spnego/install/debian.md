# Пересборка nginx с spnego-http-auth-nginx-module
* [Установите чистый nginx](../../../install/debian.md)
* Узнайте версию установленного nginx
```
nginx -V
```
* Создайте переменную окружения ***NGINX_VERSION***
```
NGINX_VERSION=1.18.0
```
* Скачайте и распакайке исходники nginx и nginx-spnego-module
```
cd /tmp && wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && tar xzf nginx-${NGINX_VERSION}.tar.gz && git clone https://github.com/stnoonan/spnego-http-auth-nginx-module.git nginx-${NGINX_VERSION}/spnego-http-auth-nginx-module
```
* Перейдите в папку с распакованными исходниками nginx
```
cd /tmp/nginx-${NGINX_VERSION}
```
* Cкопируйте ***configure arguments*** установленного nginx
```
nginx -V
```
* Выполните конфигурацию сборки со скопированными параметрами добавив параметр ***--add-module=spnego-http-auth-nginx-module***
```
./configure
--prefix=/etc/nginx
...
--add-module=spnego-http-auth-nginx-module
```
* Запустите сборку
```
sudo make && sudo make install
```