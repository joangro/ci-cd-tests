FROM python:3.7

ADD . /app

WORKDIR /app

EXPOSE 8080

RUN pip install Flask

CMD ["python", "main.py"]
