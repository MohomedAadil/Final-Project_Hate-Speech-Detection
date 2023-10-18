FROM python:3.11.3
WORKDIR /FlaskRestAPI
COPY . /FlaskRestAPI/

RUN pip install --upgrade pip

ADD requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 3000
CMD python ./app.py