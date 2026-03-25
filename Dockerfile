FROM python:3.14-slim

WORKDIR /app 

COPY requirments.txt .
RUN pip install --no-cache-dir -r requirments.txt

COPY Backend/ ./Backend
COPY Frontend/ ./Frontend

RUN ls -la ./Backend/ && ls -la ./Frontend/ 

EXPOSE 8501