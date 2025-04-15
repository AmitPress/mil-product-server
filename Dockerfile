FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/mil_product_server
RUN python manage.py makemigrations 
RUN python manage.py migrate
EXPOSE 3000
CMD ["daphne", "-p", "3000", "-b", "0.0.0.0", "mil_product_server.asgi:application"]