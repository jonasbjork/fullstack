FROM python:3.13-slim

WORKDIR /app

COPY src/requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt
COPY src/app.py .

ENV NAMN="anna"
EXPOSE 8080

CMD ["python", "app.py"]
