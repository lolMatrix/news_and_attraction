FROM python:3

COPY . .

RUN apt update
RUN apt install --assume-yes p7zip-full -y
RUN 7z x tomitaworker/tomita/tomita-parser.7z
RUN mv tomita-parser tomitaworker/tomita
RUN chmod +x tomitaworker/tomita/tomita-parser
RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]
