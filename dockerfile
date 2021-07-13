FROM python:3.9

WORKDIR /Scanner
COPY . .

RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

CMD ["echo", "override entrypoint to correct project"]