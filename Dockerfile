FROM ubuntu:latest
MAINTAINER Josh Zwiebel "josh.zwiebel@uwaterloo.ca"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /application
WORKDIR /application
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["application.py"]