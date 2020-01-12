FROM python:alpine

ENV PYTHONPATH api

WORKDIR /api

VOLUME /usr/share/html

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "api" ]
