FROM python:3.13
EXPOSE 5000
WORKDIR /app
COPY requirement.txt .
RUN pip install -r requirement.txt
COPY . .
CMD ["flask","run","--host","0.0.0.0"]