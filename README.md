# dynamodb-music

# Comandos para rodar 

# Criando ambiente virtual 
```bash
python -m venv env
source env/bin/activate  #  Linux/macOS
env\Scripts\activate.bat  # Windows
```

# Instalando as dependencias 

```bash
pip install -r requirements.txt
```

#Rodando o docker 

```
docker build -t dynamodb:1.0 .
docker run -p 8080:8080 dynamodb:1.0
```
