FROM python:3.11-slim

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","-m","flask", "--app=app","run","--host=0.0.0.0"]
