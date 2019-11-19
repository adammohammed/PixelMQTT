FROM python:3-alpine

ENV FLASK_APP=colorchanger
ENV FLASK_ENV=development

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY colorchanger /app/colorchanger

WORKDIR /app

ENTRYPOINT ["flask"]
CMD ["run"]