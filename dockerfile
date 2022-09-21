FROM python

RUN apt update -y && \
    apt install telnet -y && \
    rm -rf /var/lib/apt/lists/*

COPY us-venv /data_copier

RUN pip install -r /data_copier/requirements.txt