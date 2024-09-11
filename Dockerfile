
FROM python
COPY main.py .
RUN apt-get update && apt-get install -y python3
RUN /bin/sh pip3 install discord.py
RUN python3 discord.py
