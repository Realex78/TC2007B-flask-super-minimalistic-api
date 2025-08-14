FROM python:latest

WORKDIR /app
COPY . .

RUN pip install Flask

EXPOSE 7878
CMD ["python", "app.py"]
