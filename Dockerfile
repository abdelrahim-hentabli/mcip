
FROM python:3-alpine

WORKDIR /usr/src/app
COPY main.py .
RUN pip install discord.py
CMD [ "python", "main.py" ]
