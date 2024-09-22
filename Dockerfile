
FROM python:3-alpine

ARG DISCORD_API_TOKEN=NOT_A_VALID_API_TOKEN

WORKDIR /usr/src/app
COPY main.py .
RUN apk update && apk add --no-cache curl
RUN pip install discord.py
CMD [ "python", "main.py" ]
