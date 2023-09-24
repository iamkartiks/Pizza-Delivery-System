FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /Pizza-Delivery-System

COPY . /Pizza-Delivery-System

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
