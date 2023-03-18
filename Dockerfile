FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN mkdir /controle_pav
WORKDIR /controle_pav
COPY requirements.txt /controle_pav/
RUN pip install -r requirements.txt
COPY . /controle_pav/

EXPOSE 8000

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
