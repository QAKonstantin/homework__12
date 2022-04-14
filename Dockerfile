FROM jenkins/jenkins:lts

USER root

RUN apt update && apt install -y \ 
    build-essential \
    python3 \
    python3-venv