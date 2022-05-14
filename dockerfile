# Pull base image
FROM python:3.7
# Set environment varibles
WORKDIR /code/
# Install dependencies
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY . /code/
RUN apt-get install python3-pip -y
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "server.py"]
