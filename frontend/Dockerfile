FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /frontend

COPY . .

EXPOSE 5000

CMD ["python", "-m", "http.server", "5000"]