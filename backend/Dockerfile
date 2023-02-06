FROM python:3.9 as base
  WORKDIR /backend
  # this is done before so I don't need to re-install
  # dependencies every time I change the code
  COPY requirements.txt ./
  RUN pip install -r ./requirements.txt

# docker build -t test --target test ./backend/ && docker run test 
FROM base as test
  COPY server.py ./
  COPY ./test/test_api.py ./
  CMD pytest

FROM base as run-dev
  CMD ["python", "server.py"]

FROM base as run-prod
  CMD ["gunicorn", "-b", ":5001", "server:app"]