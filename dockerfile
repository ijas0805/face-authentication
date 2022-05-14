# Pull base image
FROM python:3.7
# Set environment varibles
WORKDIR /code/
# Install dependencies
RUN apt-apt update
RUN apt-apt install ffmpeg libsm6 libxext6  -y
COPY . /code/
RUN apt-get install python3-pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "server.py"]
