FROM python:3.11-slim

WORKDIR /app

COPY ./uploads . 

CMD python3 -m http.server 8000 
