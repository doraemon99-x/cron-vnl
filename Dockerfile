# Gunakan image Python resmi dari Docker Hub
FROM python:3.9-slim

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Buat directory kerja di container
WORKDIR /app

# Salin file requirements.txt ke dalam container
COPY requirements.txt /app/

# Install dependencies dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file dari direktori lokal ke container
COPY . /app/

# Expose port yang digunakan oleh Flask
EXPOSE 5000

# Perintah untuk menjalankan aplikasi
CMD ["python", "vido.py"]
