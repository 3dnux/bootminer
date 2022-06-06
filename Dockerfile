FROM ubuntu:21.04

RUN DEBIAN_FRONTEND="noninteractive"
ARG ssh_prv_key
ARG ssh_pub_key

# run update and upgrade
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install tzdata

RUN apt-get -y install python3 pip

RUN apt-get -y install git openssh-server vim curl mc


RUN mkdir -p /var/www/html/

# Authorize SSH Host
RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh;

# Add the keys and set permissions
RUN echo "$ssh_prv_key" > /root/.ssh/id_rsa && \
    echo "$ssh_pub_key" > /root/.ssh/id_rsa.pub && \
    chmod 600 /root/.ssh/id_rsa && \
    chmod 600 /root/.ssh/id_rsa.pub


# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99


# Install python libs
RUN pip install pika
RUN pip install selenium
RUN pip install requests
RUN pip install bs4
RUN pip install amazoncaptcha
RUN pip install webdriver_manager


# container build command
# > $ docker build -t worker .
# command to run the container
# > $ $ docker run --add-host=rabbit:YOUR_IP  -v $(pwd)/:/var/www/html -it worker  bash