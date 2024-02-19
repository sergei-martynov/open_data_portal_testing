FROM python:3.11

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg

# Установка последней версии Google Chrome
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
#     && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
#     && apt-get update \
#     && apt-get install -y google-chrome-stable

# Установка Google Chrome c указанием версии
ENV CHROME_VERSION=114.0.5735.90-1
RUN wget --no-check-certificate https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb
RUN dpkg -i google-chrome-stable_${CHROME_VERSION}_amd64.deb || apt -y -f install
RUN rm google-chrome-stable_${CHROME_VERSION}_amd64.deb

# Установка последней версии chromedriver и добавление в её в PATH
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip -o /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
RUN rm /tmp/chromedriver.zip
ENV PATH="/usr/local/bin:${PATH}"

# Установка Firefox и Geckodriver
# firefox-esr (для debian)
RUN apt-get update && apt-get install -y firefox-esr
RUN apt-get install -y -qq wget && \
    wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz && \
    tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin && \
    rm /tmp/geckodriver.tar.gz

# Копирование текущего проекта в дирректорию контейнера
COPY . /app
WORKDIR /app

# Создание заранее папок для взаимодействия из коммандной строки 
RUN mkdir allure-results \
    downloads \
    screenshots

# Обновление pip
RUN pip install --upgrade pip

# Установка зависимостей из requirements.txt
RUN pip install -r requirements.txt


CMD ["pytest", "-s", "-v", "tests/*", "--alluredir=allure-results"]