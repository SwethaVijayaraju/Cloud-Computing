FROM python:3.10.7
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

COPY app app
WORKDIR /app

EXPOSE 8000

CMD ["python", "app/manage.py", "migrate"]
CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]