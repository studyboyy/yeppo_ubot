FROM nikolaik/python-nodejs:python3.10-nodejs20
RUN apt-get update -y

WORKDIR /app

COCB . .

RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

CMD ["python", "-m", "NEZABOT"]
