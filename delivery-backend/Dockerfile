FROM python:3.8

RUN apt-get update && \
    apt-get install -y gdal-bin

ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

WORKDIR /delivery-backend

COPY requirements.txt /delivery-backend
RUN pip3 install -r requirements.txt

RUN echo "PS1='\[\033[31m\](\h) \[\033[00;36m\]\u\[\033[01;32m\] \w \[\033[00m\]$ '" >> ~/.bashrc

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /