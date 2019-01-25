FROM python:3.7-stretch
COPY src/ /src
COPY requirements.txt /src/requirements.txt
WORKDIR /src
RUN ls -la /
RUN ls -la /src
RUN pip install -r /src/requirements.txt

