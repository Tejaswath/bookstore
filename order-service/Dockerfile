FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install flask flask_cors
EXPOSE 5002
CMD ["python", "order_service.py"]