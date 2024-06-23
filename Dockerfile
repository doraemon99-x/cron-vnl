# Gunakan image python sebagai base
FROM python:3.9-slim

# Atur working directory di dalam container
WORKDIR /app

# Salin requirements.txt dan install dependencies (jika ada)
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# Salin semua file ke working directory
COPY . .

# Jalankan script
CMD ["python", "cronjob.py"]
