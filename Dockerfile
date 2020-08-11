FROM python:3.8

COPY . /app
WORKDIR /app

ADD Pipfile Pipfile
ADD Pipfile.lock Pipfile.lock
RUN pip install pipenv && \
    pipenv install --dev --system --deploy

CMD uvicorn main:app --workers 4 --host 0.0.0.0 --port 8000 --reload
