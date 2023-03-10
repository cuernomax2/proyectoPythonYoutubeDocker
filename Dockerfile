FROM python:3

WORKDIR /usr/src/app

RUN pip install requirements.txt

COPY ./app /usr/src/app/

CMD ["python", "main.py"]
