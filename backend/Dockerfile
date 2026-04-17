# Usa uma imagem oficial do Python, versão leve
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /code

# Copia o arquivo de dependências primeiro (ajuda no cache do Docker)
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o resto do código da pasta backend para dentro do container
COPY . .

# (O comando para rodar o servidor já está lá no docker-compose.yml)