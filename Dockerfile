FROM python:3

WORKDIR /ADAccountManager

ADD . /ADAccountManager

RUN pip install -r requirements.txt

EXPOSE 80

ENV __name__ __main__


CMD ["python", "start.py"]