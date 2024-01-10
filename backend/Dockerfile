# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container to /usr/src/app
WORKDIR /usr/src/app/

RUN apt-get update && apt-get install -y \
    ghostscript \
    tesseract-ocr \
    tesseract-ocr-deu \
    pngquant \
    unpaper \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements.txt first to leverage Docker cache
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run the Python script to start the app
CMD python generate_secret.py && python main.py