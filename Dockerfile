FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /Pizza-Delivery-System
WORKDIR /Pizza-Delivery-System
COPY . /Pizza-Delivery-System
RUN apt-get update
RUN apt-get update && apt-get install -y iputils-ping
RUN pip install -r requirements.txt
EXPOSE 8000



