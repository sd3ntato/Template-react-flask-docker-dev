FROM python:3.9

WORKDIR /backend

# this is done before so I don't need to re-install
# dependencies every time I change the code
COPY requirements.txt ./
RUN pip install -r ./requirements.txt

# COPY server.py ./ # this is done in docker-compose

CMD ["python", "server.py"]