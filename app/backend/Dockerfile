FROM python:3.9

WORKDIR /home/backend

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app/ app

CMD ["python", "-m", "app.main"]
