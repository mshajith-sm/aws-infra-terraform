FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y wget unzip git curl && \
    wget https://releases.hashicorp.com/terraform/1.13.0/terraform_1.13.0_linux_amd64.zip && \
    unzip terraform_1.13.0_linux_amd64.zip && \
    mv terraform /usr/local/bin/

USER jenkins