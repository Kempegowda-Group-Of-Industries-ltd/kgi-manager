FROM python:3.12-slim

# Install system dependencies including D-Bus and Xvfb
RUN apt-get update && \
    apt-get install -y \
    dbus \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Set up a virtual display (Xvfb) to handle graphical operations
RUN Xvfb :99 -screen 0 1024x768x24 &

# Set the environment variable for DISPLAY to use the virtual display
ENV DISPLAY=:99

# Copy the requirements file to the Docker image
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt

# Copy the rest of the application code into the Docker image
COPY . /app

# Set the working directory inside the Docker image
WORKDIR /app

# Define the command to run the Streamlit application
CMD ["streamlit", "run", "app.py"]
