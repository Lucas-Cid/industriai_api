# Base image com Python e Node.js
FROM python:3.11

# Instalar dependências do sistema (build-essential, curl)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    openjdk-17-jre-headless \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar Node.js v18.x
RUN curl -sL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar o Serverless Framework globalmente e plugins necessários para Python
RUN npm install -g serverless@3 \
    serverless/utils \
    serverless-offline \
    serverless-dynamodb \
    serverless-offline-sqs

# Set working directory for application code
WORKDIR /app

# Copy application code
COPY . .

RUN pip install --no-cache-dir -r ./app/requirements.txt

# Expose port for serverless-offline and DynamoDB local
EXPOSE 3000

# Ensure start.sh is executable
RUN chmod +x ./app/start.sh

CMD ["bash", "./start.sh"]
