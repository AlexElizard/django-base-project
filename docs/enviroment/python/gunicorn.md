* Измените конфигурацию gunicorn в файле `config/gunicorn.conf.py` согласно [документации](https://docs.gunicorn.org/en/latest/settings.html)
* Сгенерируйте файлы socket и service с помощью python-скрипта или создайте их согласно [документации](https://docs.gunicorn.org/en/latest/deploy.html#systemd)
* Запустите сервис и добавьте его в автозагрузку
```
sudo systemctl enable --now gunicorn-{PROJECT_NAME}.service
```

### Скрипт для генерации файлов сокета и сервиса
**Примечания:** 
* Запускать из под `sudo`
* Скрипт генерирует сервис и сокет в формате `gunicorn-{PROJECT_NAME}.socket` и `gunicorn-{PROJECT_NAME}.service`
```python
import os
import pwd

BASE_DIR = os.getcwd()
PROJECT_NAME = os.path.basename(os.getcwd())
USER = pwd.getpwuid(os.getuid())
NGINX_USER = 'www-data'
PIPENV_PATH = '/usr/local/bin/pipenv'
SYSTEMD_PATH = '/etc/systemd/system'

###################
# Создание сокета #
###################
socket_output = f'''[Unit]
Description={PROJECT_NAME} socket

[Socket]
ListenStream=/run/gunicorn-{PROJECT_NAME}.sock
SocketUSER={NGINX_USER}

[Install]
WantedBy=sockets.target'''

with open(f'{SYSTEMD_PATH}/gunicorn-{PROJECT_NAME}.socket ', 'w') as file:
    file.write(socket_output)

####################
# Создание cервиса #
####################
service_output = f'''[Unit]
Description={PROJECT_NAME} daemon
Requires=gunicorn-{PROJECT_NAME}.socket
After=network.target

[Service]
Type=notify
USER={USER}
Group={USER}
RuntimeDirectory=gunicorn
WorkingDirectory={BASE_DIR}
ExecStart={PIPENV_PATH} run gunicorn --config config/gunicorn.conf.py config.wsgi
ExecReload=/bin/kill -s HUP $MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true

[Install]
WantedBy=multi-USER.target
'''

with open(f'{SYSTEMD_PATH}/gunicorn-{PROJECT_NAME}.service', 'w') as file:
    file.write(service_output)
```
