FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENV EVEPORT=5000
ENV MONGODB=walkup-mongdb
ENV MONGOPORT=27017
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE 5000
CMD ["python","run.py","runserver"]
