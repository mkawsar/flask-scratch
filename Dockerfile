FROM python:3.8

# USER app
ENV PYTHONUNBUFFERED 1
# RUN mkdir /db
#RUN chown app:app -R /db

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
COPY .flaskenv.example /code/.flaskenv
RUN pip install -r requirements.txt
ADD . /code/

EXPOSE 5000