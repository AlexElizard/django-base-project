#####################
# Gunicorn settings #
#####################
workers = 3
reload = True

#####################################
# Creation service and socket files #
#####################################
if __name__ == '__main__':
    from pathlib import Path

    DEFAULT_BASE_DIR = Path(__file__).absolute().parents[1]
    BASE_DIR = input(f"Project directory [default: {DEFAULT_BASE_DIR}]: ") or DEFAULT_BASE_DIR

    DEFAULT_NAME = f"gunicorn-{BASE_DIR.name}"
    NAME = input(f"Socket/Service name [default: {DEFAULT_NAME}]: ") or DEFAULT_NAME

    DEFAULT_USER = Path(BASE_DIR).owner()
    USER = input(f"User [default: {DEFAULT_USER}]: ") or DEFAULT_USER

    DEFAULT_NGINX_USER = 'www-data'
    NGINX_USER = input(f"Nginx user [default: {DEFAULT_NGINX_USER}]: ") or DEFAULT_NGINX_USER

    DEFAULT_PIPENV_PATH = '/bin/pipenv'
    PIPENV_PATH = input(f"Pipenv path [default: {DEFAULT_PIPENV_PATH}]: ") or DEFAULT_PIPENV_PATH

    # Socket template
    socket_output = f'''[Unit]
    Description={NAME}-socket

    [Socket]
    ListenStream=/run/{NAME}.sock
    SocketUser={NGINX_USER}

    [Install]
    WantedBy=sockets.target'''

    # Service template
    service_output = f'''[Unit]
    Description={NAME}-daemon
    Requires={NAME}.socket
    After=network.target

    [Service]
    Type=notify
    User={USER}
    Group={USER}
    RuntimeDirectory=gunicorn
    WorkingDirectory={BASE_DIR}
    ExecStart={PIPENV_PATH} run gunicorn --config config/gunicorn.py config.wsgi
    ExecReload=/bin/kill -s HUP $MAINPID
    KillMode=mixed
    TimeoutStopSec=5
    PrivateTmp=true

    [Install]
    WantedBy=multi-user.target
    '''

    print("\n\nCheck settings: \n\nSocket:\n" + socket_output, "Service:\n" + service_output, sep='\n\n')
    choice = input("It's correct? y or n: ")
    if choice == 'y':
        with open(f"/etc/systemd/system/{NAME}.socket", "w") as file:
            file.write(socket_output)

        with open(f"/etc/systemd/system/{NAME}.service", "w") as file:
            file.write(service_output)

        print("Enter the command to add the service to startup:")
        print(f"sudo systemctl enable --now {NAME}.service")
    else:
        print('Please rerun script')
