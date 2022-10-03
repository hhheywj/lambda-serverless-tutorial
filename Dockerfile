FROM public.ecr.aws/lambda/python@sha256:25c6bcc63244a4c64d5c6593529dbc51f279ed4a2b731e9ae5a6fe839d8be69d as build

FROM public.ecr.aws/lambda/python@sha256:25c6bcc63244a4c64d5c6593529dbc51f279ed4a2b731e9ae5a6fe839d8be69d

RUN pip install psycopg2-binary
RUN pip install requests

COPY main.py ./
CMD [ "main.handler" ]
