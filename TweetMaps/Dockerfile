FROM python:3

ENV PYTHONUNBUFFERED 1
RUN git clone https://github.com/miguelpantoja89/CBD-TweetMaps .
RUN mkdir /TweetMaps
WORKDIR /TweetMaps
COPY . /TweetMaps/
RUN pip install -r requirements.txt