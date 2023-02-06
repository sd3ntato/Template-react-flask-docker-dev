FROM python:3.9 as base
  WORKDIR /backend
  # this is done before so I don't need to re-install
  # dependencies every time I change the code
  COPY requirements.txt ./
  RUN pip install -r ./requirements.txt

# docker build -t test --target test ./backend/
# docker run test 
FROM base as test
  COPY server.py ./
  COPY ./test/test_api.py ./
  CMD pytest

FROM base as run-server
  # COPY server.py ./ # this is done in docker-compose
  CMD ["python", "server.py"]