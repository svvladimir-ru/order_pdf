# order_pdf

* order_pdf

Сервис который преобразует введеные данные в html шаблон с тегами <p> и далее преобразует html шаблон в pdf

### Требования


[Python](https://www.python.org/downloads/) v3.7 +  для запуска.
Установите зависимости и виртуальное окружение и запустите сервер.

```sh
$ pip install virtualenv
$ virtualenv 'название виртуального окружения', либо python3 -m venv 'название виртуального окружения'
$ venv 'название виртуального окружения'/Scripts(или bin для linux)/activate
$ pip install -r requirements.txt
$ python main.py
```

Запуск через докер

[Docker](https://www.docker.com/)

Установка для linux
```sh
$ sudo apt update
$ sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository \
$ "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$ (lsb_release -cs) \
$ stable"
$ sudo apt update
$ sudo apt install docker-ce -y
```
После установки выполнить следующие действия:
1. В корневой директории проекта создайте образ командой docker build -t <тут введите имя образа> .
2. Запустите контейнер командой docker run -it -p 8000:8000 <имя образа>
3. Ввести данные
4. Запустить контейнер снова
5. Командой docker ps узнать container id и через команду docker exec -it <container id> ls можно будет увидить созданые файлы. Через команду cat order.html можно будет просмотреть файл order.html



## Авторы

* **Vladimir Svetlakov** - [svvladimir-ru](https://github.com/svvladimir-ru)
