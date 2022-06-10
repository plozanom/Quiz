FROM python:3.9-bullseye

#RUN apt-get install python3
RUN python -m ensurepip
RUN python -m pip install --upgrade pip setuptools

WORKDIR /app

COPY . /app/

RUN pip --no-cache-dir install -r requirements.txt

CMD ["python", "main.py"]