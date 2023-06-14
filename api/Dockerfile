FROM python:3.11
COPY pyproject.toml .
COPY README.md .
COPY poetry.lock .
COPY api api
RUN pip3 install --no-cache-dir poetry==1.4.2
RUN poetry install
CMD poetry run uvicorn --app-dir api --host 0.0.0.0 --port 80 main:app
