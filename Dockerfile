FROM python:3.8
RUN apt-get clean \
    && apt-get -y update
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt --src /usr/local/src
EXPOSE 5000
CMD [ "python", "app.py" ]