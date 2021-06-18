* Установите зависимости, необходимые для сборки Python
```
sudo apt update && sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev
```
* Создайте переменную окружения ***PYTHON_VERSION***. <br>Cписок доступных версий можно увидеть на [странице загрузки Python](https://www.python.org/downloads/source/)
```
PYTHON_VERSION=3.9.1
```
* Загрузите и распакуйте исходный код
```
cd ~ && mkdir -p python && cd python && wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && tar -xf Python-${PYTHON_VERSION}.tgz
```
* Выполните `configure` сценарий:
```
cd Python-${PYTHON_VERSION} && ./configure --enable-optimizations --prefix=/opt/python${PYTHON_VERSION} 
```
* Соберите Python. Значение параметра `-j` должно соответствовать числу, полученному при выводе команды `nproc`
```
make -j 2
```
* Установите собранный Python
```
sudo make altinstall && cd ~
```