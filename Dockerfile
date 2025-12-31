# Use a lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Set environment variable default (optional)
ENV APP_PORT=5000

# Run the app using environment variable
CMD ["sh", "-c", "python app.py"]

