# pull official python alpine image
FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive


# Making source and static directory
RUN mkdir /stats-monitor
RUN mkdir /stats-monitor/static

# Creating Work Directory
WORKDIR /stats-monitor

# Adding mandatory packages to docker
RUN apt update && apt install -y \
    postgresql \
    curl \
    git \
    python3 \
    python3-pip \
    openssh-server
# Installing temporary packages required for installing requirements.pip 
RUN apt install -y build-essential \
    python3-dev \ 
    libffi-dev \ 
    libpq-dev \
    jq \
    netcat \
    musl-dev 

# Update pip
RUN pip3 install --upgrade pip

# Installing requirements.pip from project
COPY ./requirements.pip /scripts/
RUN pip3 install --no-cache-dir -r /scripts/requirements.pip

#RUN cd /stats-monitor/ && cd yajsapi && git checkout b0.3 && cd examples/ && yarn

# CMD will run when this dockerfile is running
CMD ["bash", "-c", "/wait-for-it.sh postgres:5432 -- celery -A core worker -l INFO"]
