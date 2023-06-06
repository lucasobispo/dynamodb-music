# Use a imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho como /app
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências usando o pip
RUN pip install --no-cache-dir -r requirements.txt

# Copie a pasta app para o diretório de trabalho
COPY ./app .

# Exponha a porta 8000
EXPOSE 8080

# Defina o comando de inicialização do servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
