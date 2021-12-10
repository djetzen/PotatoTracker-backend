FROM python:3.10.1-alpine

RUN apk --update --no-cache add curl && rm -rf /var/cache/apk/*

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 6543

CMD ["python3","-m", "backend.app"]

