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
5. sudo apt install --assume-yes p7zip-full -y
6. 7z x tomitaworker/tomita/tomita-parser.7z
7. mv tomita-parser tomitaworker/tomita
8. chmod +x tomitaworker/tomita/tomita-parser
9. pip3 install virtualenv
10. python3 -m virtualenv venv
11. source venv/bin/activate
12. pip install -r requirements.txt
13. python main.py
14. 
Сервер django автоматически запускается вместе с краулером

Для запуска Word2Vec необходимо при запущеном проекте выполнить:
1. cd word2vecworker
2. Обучение модели python3 word_2_vec_gen.py
3. Поиск синонимов по словам python3 word_2_vec_user.py


