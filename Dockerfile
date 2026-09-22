FROM python:3.13
EXPOSE 5000
WORKDIR /app
COPY requirement.txt .
RUN pip install --no-cache-dir --updrade -r requirement.txt
COPY . .
CMD ["/bin/bash","docker-entrypoint.sh"]