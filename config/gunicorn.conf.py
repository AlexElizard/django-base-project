######################
# Настройки gunicorn #
######################
workers = 3
reload = True

##############################################
# Скрипт по созданию service и socket файлов #
##############################################
if __name__ == '__main__':
    from pathlib import Path

    BASE_DIR = Path(__file__).absolute().parents[1]
    PROJECT_NAME = BASE_DIR.name
    USER = Path(BASE_DIR).owner()
    NGINX_USER = 'www-data'
    PIPENV_PATH = '/usr/local/bin/pipenv'
    SYSTEMD_PATH = '/etc/systemd/system'

    # Шаблон сокета
    socket_output = f'''[Unit]
    Description={PROJECT_NAME}-socket

    [Socket]
    ListenStream=/run/gunicorn-{PROJECT_NAME}.sock
    SocketUser={NGINX_USER}

    [Install]
    WantedBy=sockets.target'''

    # Шаблон cервиса
    service_output = f'''[Unit]
    Description={PROJECT_NAME}-daemon
    Requires=gunicorn-{PROJECT_NAME}.socket
    After=network.target

    [Service]
    Type=notify
    User={USER}
    Group={USER}
    RuntimeDirectory=gunicorn
    WorkingDirectory={BASE_DIR}
    ExecStart={PIPENV_PATH} run gunicorn --config config/gunicorn.conf.py config.wsgi
    ExecReload=/bin/kill -s HUP $MAINPID
    KillMode=mixed
    TimeoutStopSec=5
    PrivateTmp=true

    [Install]
    WantedBy=multi-user.target
    '''

    print("Проверьте настройки: \nСокет:\n" + socket_output, "Сервис:\n" + service_output, sep='\n\n')
    choice = input('Все верно? y or n: ')
    if choice == 'y':
        with open(f'{SYSTEMD_PATH}/gunicorn-{PROJECT_NAME}.socket', 'w') as file:
            file.write(socket_output)

        with open(f'{SYSTEMD_PATH}/gunicorn-{PROJECT_NAME}.service', 'w') as file:
            file.write(service_output)

        print('Введите команду для добавления сервиса в автозагрузку:')
        print(f'sudo systemctl enable --now gunicorn-{PROJECT_NAME}.service')
    else:
        print('Измените необходимые параметры в файле скрипта')
