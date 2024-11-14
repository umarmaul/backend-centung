# Gunakan base image Python
FROM python:3.10-slim

# Instal Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Tambahkan Poetry ke PATH
ENV PATH="/root/.local/bin:$PATH"

# Tentukan work directory di container
WORKDIR /app

# Salin file proyek ke container
COPY . .

# Instal dependensi proyek menggunakan Poetry
RUN poetry install

# Jalankan perintah untuk menjalankan server (sesuaikan dengan kebutuhan)
CMD ["poetry", "run", "start"]
