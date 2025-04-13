FROM public.ecr.aws/lambda/python:3.11

WORKDIR /var/task

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY api_serverless api_serverless/
COPY .env .env

CMD ["api_serverless.main.handler"]