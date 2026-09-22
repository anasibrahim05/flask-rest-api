FROM python:3.13
EXPOSE 5000
WORKDIR /app
COPY requirement.txt .
RUN pip install --no-cache-dir --updrade -r requirement.txt
COPY . .
CMD ["gunicorn","--bind","0.0.0.0:80","app:create_app()"]