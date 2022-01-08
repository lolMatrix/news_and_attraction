## Куросовая 
Драчев, Торбин, Фильчагин, Аншаков
## Стек
- Requests
- BeautifulSoup
- django
- mongodb
- pyspark
- threading
- остальное в процессе будет добавляться 

### Настройка проекта
По пути ./config/config.txt есть конфигурационный файл. В нем прописаны настройки базы данных mongodb.
- db_name - название базы данных
- collection - название коллекции
- host - название хоста (например: localhost, www.exemple.com)
- port - номер порта (по умолчанию в mongodb: 27017)

### Запуск проекта 
Запуск программного кода в ОС Linux Ubuntu
Необходимо перед началом настройки проекта, настроить базу данных mongodb. После настройки скачать проект: 
1. git clone https://github.com/lolMatrix/news_and_attraction.git 
В проекте используется python 3-ей версии. Устанавливаем из репозитория Ubuntu: 
2. sudo apt update
3. sudo apt install python3 && sudo apt install python3-pip
4. pip3 install virtualenv
5. python3 -m virtualenv venv
6. source venv/bin/activate
7. pip install –r requirements.txt
8. python main.py

Сервер django автоматически запускается вместе с краулером


