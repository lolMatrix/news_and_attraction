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
1. активация venv .\env\Scripts\activate
2. запуск проекта python3 main.py

Сервер django автоматически запускается вместе с краулером


