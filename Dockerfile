FROM python:3.11

WORKDIR /app

COPY install_list.txt .

RUN pip install --no-cache-dir -r install_list.txt

COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]