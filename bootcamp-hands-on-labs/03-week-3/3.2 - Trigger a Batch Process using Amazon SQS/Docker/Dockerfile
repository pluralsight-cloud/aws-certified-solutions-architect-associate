FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install awscli boto3 Pillow

ADD GetAndResizeImages.py /

CMD ["/GetAndResizeImages.py"]