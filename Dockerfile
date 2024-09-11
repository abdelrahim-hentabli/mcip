
FROM python:3-alpine

WORKDIR /usr/src/app
COPY main.py .
RUN apk update && apk add --no-cache curl
RUN pip install discord.py
CMD [ "python", "main.py" ]
