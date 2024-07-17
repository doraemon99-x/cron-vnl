# Gunakan image Node.js resmi dari Docker Hub
FROM node:14

# Buat directory kerja di container
WORKDIR /app

# Salin file package.json dan package-lock.json ke dalam container
COPY package*.json ./

# Install dependencies dari package.json
RUN npm install

# Salin semua file dari direktori lokal ke container
COPY . .

# Expose port yang digunakan oleh aplikasi
EXPOSE 5000

# Perintah untuk menjalankan aplikasi
CMD ["npm", "start"]
