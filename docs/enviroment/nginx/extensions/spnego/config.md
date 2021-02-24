# Настрока nginx
* Установите и настройке [kerberos](../../../../kerberos/install/debian.md)
* Добавьте параметры auth_gss по необходимым маршрутам
```
# /etc/nginx/conf.d/example.conf

server {
    ...
   
    location /sso {                                                     # added string
        auth_gss on;                                                    # added string          
        auth_gss_realm DOMAIN.LOCAL;                                    # added string
        auth_gss_keytab /etc/krb5.keytab;                               # added string
        auth_gss_service_name HTTP/example.com;                         # added string
        auth_gss_allow_basic_fallback on;                               # added string
        try_files $uri @backend;                                        # added string
    }

    location @backend {
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-User $remote_user;                 # added string
        proxy_redirect off;
        proxy_pass http://unix:/run/gunicorn-example.sock;
    }
}
```
## Многодоменная аутентификация
* [Создайте единый keytab-файл и настройте krb5](../../../../kerberos/multidomain.md)
* Измените конфиг nginx
```
# /etc/nginx/conf.d/example.conf

server {
    ...
   
    location /sso {
        auth_gss on;        
         # auth_gss_realm DOMAIN.LOCAL;
        auth_gss_format_full on;                       # append string
        auth_gss_keytab /etc/krb5_multidomain.keytab;  # change string
        auth_gss_allow_basic_fallback on;
        try_files $uri @backend;
    }
    
    ...
}
```