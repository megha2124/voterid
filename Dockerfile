FROM python:3.12-slim

WORKDIR /test

RUN apt-get update && \
    apt-get install -y python3-tk && \
    rm -rf /var/lib/apt/lists/*

COPY . .

CMD [ "python", "star.py" ]


# # Use the official Python image
# FROM python:3.12-slim

# # Set the working directory
# WORKDIR /app

# # Copy the application into the container
# COPY app.py .

# # Run the application
# CMD ["python", "app.py"]