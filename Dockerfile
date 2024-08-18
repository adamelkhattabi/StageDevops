FROM python:3.9-slim-buster

# Install PostgreSQL client and create a non-root user
RUN apt-get update && apt-get install -y postgresql-client && \
    useradd -m myuser

# Set up the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Create and activate virtual environment
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Change ownership of the app directory to the non-root user
RUN chown -R myuser:myuser /app

# Switch to the non-root user
USER myuser

# Run the application
CMD ["./wait-for-it.sh", "db", "5432", "--", "python", "app.py"]