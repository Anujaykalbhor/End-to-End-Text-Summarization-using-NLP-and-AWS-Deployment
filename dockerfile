# Use a base image with Python
FROM python:3.9-slim

# Install git and git-lfs
RUN apt-get update && apt-get install -y git git-lfs

# Set the working directory
WORKDIR /app

# Clone your repository
RUN git lfs clone https://github.com/Anujaykalbhor/End-to-End-Text-Summarization-using-NLP-and-AWS-Deployment.git .

# Or, if you're using a local copy
# COPY . .

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the correct port
EXPOSE 8000

# Command to run your application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]