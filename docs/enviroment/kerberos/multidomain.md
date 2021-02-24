# Многодоменная аутентификации
* Создайте по [keytab-файлу](keytab_create.md) для каждого домена
* Объедините их командой
```
sudo ktutil

read_kt domain1.keytab
read_kt domain2.keytab
write_kt /etc/krb5_keytabs/krb5_multidomain.keytab
quit
```
* Перезапишите файл настроек kerberos
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
 # default_realm = DOMAIN.TEST
 # default_ccache_name = KEYRING:persistent:%{uid}

[realms]
 DOMAIN.LOCAL = {
  kdc = domain.local
  admin_server = domain.local
 }
 DOMAIN2.LOCAL = {               # append string
  kdc = domain2.local            # append string
  admin_server = domain2.local   # append string
 }                               # append string

[domain_realm]
 .example.com = DOMAIN.LOCAL
 example.com = DOMAIN.LOCAL
 .example.com = DOMAIN2.LOCAL       # append string
 example.com = DOMAIN2.LOCAL        # append string
```