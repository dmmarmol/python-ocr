# Use a Linux-based image as the base image
FROM ubuntu:latest

# Set the working directory
WORKDIR /app

# Install Tesseract and other dependencies
RUN apt-get update \
    && apt-get install -y tesseract-ocr \
    && apt-get install -y libtesseract-dev \
    && apt-get install -y python3-pip \
    && apt-get clean

# Install language data files for Tesseract (English)
RUN apt-get install -y tesseract-ocr-eng

# Install Python dependencies
COPY requirements.txt .
# RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Set the entrypoint command
CMD [ "python3", "script.py" ]
