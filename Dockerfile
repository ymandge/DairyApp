# Use a lightweight base image
FROM python:3.8-slim

# Set the working directory within the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY DairyApp /app/DairyApp

# Expose the port that your Flask app will run on
EXPOSE 8000

# Define the command to run your Flask app
CMD ["gunicorn", "-b", "0.0.0.0:8000", "DairyApp.__main__:make_app('test')"]
