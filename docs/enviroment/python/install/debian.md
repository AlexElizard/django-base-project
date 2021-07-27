* Установите зависимости
```
sudo apt update && sudo apt install \
build-essential \
curl \
libbz2-dev \
libffi-dev \
libgdbm-dev \
liblzma-dev \
libncurses5-dev \
libnss3-dev \
libreadline-dev \
libsqlite3-dev \
libssl-dev \
pipenv \
wget \
zlib1g-dev
```
* Создайте переменную окружения ***PYTHON_VERSION***. <br>Cписок доступных версий можно увидеть на [странице загрузки Python](https://www.python.org/downloads/source/)
```
PYTHON_VERSION=3.9.6
```
* Загрузите и распакуйте исходный код
```
cd /tmp/ \
&& wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz \
&& tar -xf Python-${PYTHON_VERSION}.tgz
```
* Выполните `configure` сценарий:
```
cd Python-${PYTHON_VERSION} \
&& sudo ./configure \
--enable-optimizations \
--prefix=/opt/Python-${PYTHON_VERSION} 
```
* Соберите Python. Значение параметра `-j` должно соответствовать числу, полученному при выводе команды `nproc`
```
make -j 4
```
* Установите собранный Python
```
sudo make altinstall
```

* Удалите файлы сборки
```
cd ~ && sudo rm -rf /tmp/Python-${PYTHON_VERSION}*
```

* Добавьте скрипт для обновления переменной окружения `PATH`
```
nano .bashrc
```
```
#########################################
# Append python bin directories to PATH #
#########################################
for path in $(find /opt/Python* -name "bin" -type d); do
  if [ -d "$path" ] && [[ ":$PATH:" != *":$path:"* ]]; then
    PATH="$path${PATH:+":$PATH"}"
  fi
done
```
* Обновите переменную `PATH`
```
source .bashrc
```