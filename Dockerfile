FROM python:3

EXPOSE 5000

LABEL maintainer="qa.com"

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "~/QA-DevOps-Project-1-main/app.py" ]