* Измените конфигурацию gunicorn в файле `config/gunicorn.conf.py` согласно [документации](https://docs.gunicorn.org/en/latest/settings.html)
* Сгенерируйте файлы socket и service согласно [документации](https://docs.gunicorn.org/en/latest/deploy.html#systemd) или с помощью python-скрипта
```
sudo python config/gunicorn.conf.py
```
* Запустите сервис и добавьте его в автозагрузку
```
sudo systemctl enable --now gunicorn-{PROJECT_NAME}.service
```