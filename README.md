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
2. cd news_and_attraction
3. sudo apt update
4. sudo apt install python3 -y && sudo apt install python3-pip -y
6. sudo apt install --assume-yes p7zip-full -y
7. 7z x tomitaworker/tomita/tomita-parser.7z
8. mv tomita-parser tomitaworker/tomita
9. chmod +x tomitaworker/tomita/tomita-parser
10. pip3 install virtualenv
11. python3 -m virtualenv venv
12. source venv/bin/activate
13. pip install –r requirements.txt
14. python main.py

Сервер django автоматически запускается вместе с краулером


