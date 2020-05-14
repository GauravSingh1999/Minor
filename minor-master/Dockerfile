FROM python:3.7
FROM ubuntu:16.04

COPY . /app

# Install CV2
RUN apt-get update && apt-get -y install g++ gcc cmake protobuf-compiler git 
RUN git clone https://github.com/opencv/opencv.git /usr/local/src/opencv
RUN cd /usr/local/src/opencv/ && mkdir build
RUN cd /usr/local/src/opencv/build && cmake -D CMAKE_INSTALL_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local/ .. && make -j4 && make install
RUN cd /app
WORKDIR /app

RUN set -xe \
    && apt-get install python-pip

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]