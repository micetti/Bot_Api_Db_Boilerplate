FROM ubuntu:latest

RUN \
  apt-get update && \
  apt-get install -y python3 python-pip cron && \
  rm -rf /var/lib/apt/lists/*

ADD crontab /etc/cron.d/python-cron

RUN chmod 0644 /etc/cron.d/python-cron

ADD requirements.txt /code/requirements.txt

RUN pip install -r code/requirements.txt

ADD scrape.py /code/scrape.py

CMD ["cron", "-f"]