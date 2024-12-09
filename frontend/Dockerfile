FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /frontend

COPY . .

EXPOSE 80

CMD ["python", "-m", "http.server", "80", "--bind", "0.0.0.0"]