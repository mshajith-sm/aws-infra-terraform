FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y \
    curl \
    unzip \
    wget \
    git

# Install AWS CLI v2
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf aws awscliv2.zip

# Install Terraform
RUN wget https://releases.hashicorp.com/terraform/1.13.0/terraform_1.13.0_linux_amd64.zip && \
    unzip terraform_1.13.0_linux_amd64.zip && \
    mv terraform /usr/local/bin/ && \
    rm terraform_1.13.0_linux_amd64.zip

USER jenkins