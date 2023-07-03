FROM python:3.8.5-alpine

# Upgrade pip
RUN pip install --upgrade pip
RUN apk add --no-cache tzdata

# Install MySQL client dependencies
RUN apk add --no-cache mariadb-dev build-base

# Copy requirements and install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy Django project to /app directory
COPY ./django /app

# Set working directory
WORKDIR /app

# Copy entrypoint script
COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Set entrypoint command
ENTRYPOINT ["/app/entrypoint.sh"]

