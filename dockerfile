# Pull base image
FROM python:3.7
# Set environment varibles
WORKDIR /code/
# Install dependencies
RUN sudo apt-apt update
RUN sudo apt-apt install ffmpeg libsm6 libxext6  -y
COPY . /code/
RUN sudo apt-get install python3-pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "server.py"]
