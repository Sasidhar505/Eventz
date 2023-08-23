
FROM python:3.11.

4WORKDIR /eventz

# The requirements.txt file should be copied before the rest of the project files
COPY requirements.txt .

# Update the package manager indexes and install any required system dependencies
# Using 'apt-get' as the package manager since the base image is Ubuntu-based
RUN apt-get update && apt-get install -y \
    # Add any required system dependencies here...
    && rm -rf /var/lib/apt/lists/*

# Install the project dependencies defined in requirements.txt
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port on which the application will listen
EXPOSE 8000

# Added an entrypoint script to check the health of the app
# The script will wait for the app to be healthy before starting gunicorn
COPY docker-entrypoint.sh /eventz/docker-entrypoint.sh
RUN chmod +x /eventz/docker-entrypoint.sh
ENTRYPOINT ["/eventz/docker-entrypoint.sh"]

# Start the application using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Eventz.wsgi"]
