
FROM python:3.11.4

WORKDIR /eventz

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# Added an entrypoint script to check the health of the app
# The script will wait for the app to be healthy before starting gunicorn
COPY docker-entrypoint.sh /eventz/docker-entrypoint.sh
RUN chmod +x /eventz/docker-entrypoint.sh
ENTRYPOINT ["/eventz/docker-entrypoint.sh"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Eventz.wsgi"]
