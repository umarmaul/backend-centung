FROM python:3.10-slim

# Instal dependensi untuk mengunduh dan menjalankan Poetry
RUN apt-get update && apt-get install -y curl

# Instal Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Tambahkan Poetry ke PATH
ENV PATH="/root/.local/bin:$PATH"

# Tentukan work directory di container
WORKDIR /app

# Salin file proyek ke container
COPY . .

# Instal dependensi proyek menggunakan Poetry
RUN poetry install --no-root

# Jalankan perintah untuk menjalankan server
CMD ["poetry", "run", "start"]
