FROM python:latest

WORKDIR /~/CambiaHealth

COPY . /~/CambiaHealth

RUN ["chmod", "777", "/~/CambiaHealth/CambiaAssignment.py"]

CMD ["/~/CambiaHealth/CambiaAssignment.py"]

