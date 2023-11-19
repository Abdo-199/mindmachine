# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container to /usr/src/app
WORKDIR /usr/src/app/

# Copy the backend directory contents into the container at /usr/src/app
COPY . .

# RUN ls /usr/src/app/ # Verify that the file is in the target directory
# RUN echo "Hello, World!" > /usr/src/app/test.txt # Write a test file to the target directory to check for permission issues
# RUN cat /usr/src/app/test.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run the Python script to start the app
CMD ["python", "main.py"]