* Пример файла конфигурации Nginx
```
# /etc/nginx/conf.d/example.conf

server {
    listen       80;
    server_name  example.com;
    access_log  /var/log/nginx/example/access.log combined;
    error_log /var/log/nginx/example/error.log error;

    # Frontend
    location / {
        root /home/user/www/example/front/build;
        try_files $uri /index.html;
    }

    # Static and Media
    location /upload {
        alias /home/user/www/example/back/media;
    }

    location /django-static {
        alias /home/user/www/example/back/static;
    }

    # Backend
    location ~^/(api|admin|swagger) {
        try_files $uri @backend;
    }

    location @backend {
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_redirect off;
        proxy_pass http://unix:/run/gunicorn-example.sock;
    }
}
```