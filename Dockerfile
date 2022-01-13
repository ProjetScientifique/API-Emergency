FROM python:3.9.9
WORKDIR /fastapi-app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ./app
CMD ["python", "./app/main.py"]

