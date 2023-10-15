FROM python:3.9

RUN mkdir /greatproject

WORKDIR /greatproject

COPY . /greatproject/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
