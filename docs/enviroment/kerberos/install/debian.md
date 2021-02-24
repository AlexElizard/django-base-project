# Синхронизация времени с сервером AD
* Измените часовой пояс
```
sudo ln -sf /usr/share/zoneinfo/Asia/Vladivostok /etc/localtime 
```
* Проверьте, что время задано верно, при необходимости скорректируйте его
```
date
sudo date --set "hh:mm"c
```
# Установка  
* Установите kerberos. Задавать реалм не нужно
```
sudo apt install krb5-user libkrb5-dev
```
* Создайте/Перезапишите файл конфигурации kerberos
```
# /etc/krb5.conf

[logging]
 default = FILE:/var/log/krb5libs.log
 kdc = FILE:/var/log/krb5kdc.log
 admin_server = FILE:/var/log/kadmind.log
 
[libdefaults]
 dns_lookup_realm = false
 ticket_lifetime = 24h
 renew_lifetime = 7d
 forwardable = true
 rdns = false
 default_realm = DOMAIN.LOCAL
 default_ccache_name = KEYRING:persistent:%{uid}

[realms]
 DOMAIN.LOCAL = {
  kdc = domain.local
  admin_server = domain.local
 }

[domain_realm]
 .example.com = DOMAIN.LOCAL
 example.com = DOMAIN.LOCAL
```
* Создайте [keytab-файл](../keytab_create.md)