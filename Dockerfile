FROM python:3.10.9

SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash pilot_project && chmod 777 /opt /run

WORKDIR /pilot_project

RUN mkdir /pilot_project/static && mkdir /pilot_project/media && chown -R pilot_project:pilot_project /pilot_project && chmod 755 /pilot_project

COPY --chown=pilot_project:pilot_project . .

RUN pip install -r requirements.txt

USER pilot_project

CMD ["gunicorn","-b","0.0.0.0:8000","pilot_project.wsgi:application"]
