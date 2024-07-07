# Gunakan image Python sebagai base
FROM python:3.9-slim

# Tetapkan variabel lingkungan untuk menghilangkan pesan buffering
ENV PYTHONUNBUFFERED=1

# Tentukan direktori kerja di dalam container
WORKDIR /app

# Salin file requirements.txt ke dalam container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode sumber ke dalam container
COPY . .

# Tentukan perintah yang akan dijalankan saat container di-start
CMD ["python", "vid.py"]
