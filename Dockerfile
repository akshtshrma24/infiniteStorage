FROM python:3.11-slim

COPY . .

CMD python3 -m http.server 8000 
