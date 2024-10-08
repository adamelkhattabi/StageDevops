FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y postgresql-client && \
    useradd -m myuser

WORKDIR /app

COPY requirements.txt .
RUN cat requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip list

COPY . .
RUN chmod +x wait-for-it.sh
RUN chown -R myuser:myuser /app

USER myuser

CMD ["./wait-for-it.sh", "db:5432", "--", "python", "app.py"]