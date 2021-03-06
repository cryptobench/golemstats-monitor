# pull official python alpine image
FROM python:3.9-alpine

# Set Environment Variable
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

# Making source and static directory
RUN mkdir /stats-monitor
RUN mkdir /stats-monitor/static

# Creating Work Directory
WORKDIR /stats-monitor

# Adding mandatory packages to docker
RUN apk update && apk add --no-cache \
    postgresql \
    zlib \
    openssh-server \
    jpeg 
# Installing temporary packages required for installing requirements.pip 
RUN apk add --no-cache --virtual build-deps \
    gcc \  
    python3-dev \ 
    libffi-dev \ 
    musl-dev \
    postgresql-dev\
    zlib-dev \
    build-base \
    cargo \
    rust \
    jpeg-dev 

# Update pip

# Installing requirements.pip from project
COPY ./requirements.pip /scripts/
RUN pip install --upgrade pip && pip install cryptography
RUN pip install --no-cache-dir -r /scripts/requirements.pip

# removing temporary packages from docker and removing cache 
RUN apk del build-deps && \
    find -type d -name __pycache__ -prune -exec rm -rf {} \; && \
    rm -rf ~/.cache/pip

# CMD will run when this dockerfile is running
CMD ["sh", "-c",  "/wait-for-it.sh postgres:5432 -- python manage.py makemigrations; python manage.py migrate; python manage.py collectstatic --no-input; daphne -u /tmp/daphne.sock -b 0.0.0.0 -p 8002 core.asgi:application"]
