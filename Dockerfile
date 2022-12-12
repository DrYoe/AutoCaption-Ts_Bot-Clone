FROM python:3.9.10
RUN apt-get -qq update
RUN apt-get -qq install -y git python3 python3-pip npm
COPY . .
RUN pip install -U -r requirements.txt
RUN chmod +x start.sh
CMD ["bash","start.sh"]
