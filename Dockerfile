FROM python:3-alpine

ADD ./ ./

RUN pip install -r requirements.txt

CMD python app.py
