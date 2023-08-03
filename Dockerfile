FROM python:3

EXPOSE 5000

LABEL maintainer="qa.com"
WORKDIR C:\Users\Admin\QA-DevOps-Project-1-main

COPY ./*.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "./app.py" ]
