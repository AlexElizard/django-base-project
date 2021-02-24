# Создание и проверка keytab-файла
* Создайте keytab-файл на стороне Active Directory
```
ktpass
 -princ HTTP/example.com@DOMAIN.LOCAL
 -mapuser user@domain 
 -pass password
 -crypto All
 -ptype KRB5_NT_PRINCIPAL 
 -out C:\keytabs\krb5.keytab
```
* Сохраните полученный keytab-файл на сервере и добавьте ему права на чтение
```
sudo chmod a+r /etc/krb5_keytabs/krb5.keytab
```
* Проверьте работоспособность kerberos-аутентификации. Должна появиться надпись
"***Authenticated to Kerberos v5***"
```
kinit -V -k -t /etc/krb5.keytab HTTP/example.com@DOMAIN.LOCAL
```
**Примечание:** в случае неуспеха проверьте домены keytab-файла командой
```
klist -K -e -t -k /etc/krb5_keytabs/krb5.keytab
```
* Удалите полученный тикет
```
kdestroy
```