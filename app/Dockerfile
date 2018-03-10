FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install Flask
RUN pip3 install --upgrade google-api-python-client
RUN pip3 install --upgrade redis
RUN pip3 install --upgrade mysqlclient

COPY . .

CMD ["python","-u","__main__.py"]
