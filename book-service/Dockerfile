FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install flask flask_cors
EXPOSE 5001
CMD ["python", "book_service.py"]