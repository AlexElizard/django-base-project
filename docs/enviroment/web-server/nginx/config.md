# Создание файла конфигурации
* Создайте файл конфигурации под ваш domain_name
```
sudo nano /etc/nginx/conf.d/domain_name.conf
```
Пример файла конфигурации
```
upstream app_server {
    # For UNIX domain socket setups
    # server unix:/tmp/gunicorn.sock fail_timeout=0;    

    # For a TCP configuration
    server 127.0.0.1:8000 fail_timeout=0;
}

server {
    listen       80;
    server_name  domain_name;
    access_log  /var/log/nginx/domain_name/access.log combined;
    error_log /var/log/nginx/domain_name/error.log error;

    # Frontend
    location / {
        root /home/user/www/frontend/build;
        try_files $uri /index.html;
    }

    # Static and Media
    location /upload {
        alias /home/user/www/backend/media;
    }

    location /django-static {
        alias /home/user/www/backend/static;
    }

    # Backend
    location ~^/(api|admin) {
        try_files $uri @backend;
    }

    location @backend {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_pass http://app_server;
    }
}
```