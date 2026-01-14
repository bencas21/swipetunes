FROM mcr.microsoft.com/devcontainers/python:3.12

# Install Node 20
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
  && apt-get update \
  && apt-get install -y nodejs \
  && npm install -g aws-cdk \
  && npm cache clean --force

# AWS CLI
RUN apt-get update && apt-get install -y awscli
