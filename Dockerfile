FROM ubuntu:latest

ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Instale o PostgreSQL, o Redis, o Python, o pip e o Celery
RUN apt-get update && apt-get install -y postgresql postgresql-contrib redis-server python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install psycopg2-binary \
    && apt-get install -y tzdata

# Configure o PostgreSQL
USER postgres

# Crie um banco de dados e um usuário para o Django
RUN /etc/init.d/postgresql start \
    && psql --command "CREATE DATABASE mydatabase;" \
    && psql --command "CREATE USER myuser WITH PASSWORD 'mypassword';" \
    && psql --command "GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;"

# Configure o Redis
USER root
RUN sed -i 's/bind 127.0.0.1/bind 0.0.0.0/' /etc/redis/redis.conf

# Defina o diretório de trabalho como /app
WORKDIR /app

# Copie o arquivo requirements.txt e instale as dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copie todo o código fonte do Django para o diretório de trabalho do contêiner
COPY . .

# Exponha a porta 8000 para o servidor Django
EXPOSE 8000

# Script de inicialização
COPY start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]
