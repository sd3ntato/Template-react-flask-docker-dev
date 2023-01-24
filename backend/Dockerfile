FROM python:3.9

WORKDIR /backend

COPY requirements.txt server.py ./

RUN pip install -r ./requirements.txt

CMD ["python", "server.py"]