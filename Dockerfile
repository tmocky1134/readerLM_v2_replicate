FROM python:3.9-slim

WORKDIR /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set the default command to run your predict script
CMD ["python", "predict.py"]
