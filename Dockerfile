FROM python:3.8

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    libatlas-base-dev gfortran nginx supervisor

RUN pip3 install uwsgi

COPY ./requirements.txt /project/requirements.txt

RUN pip3 install -r /project/requirements.txt

RUN useradd --no-create-home nginx

RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache

COPY server_configs/nginx.conf /etc/nginx/
COPY server_configs/flask-site-nginx.conf /etc/nginx/conf.d/
COPY server_configs/uwsgi.ini /etc/uwsgi/
COPY server_configs/supervisord.conf /etc/

RUN mkdir -p /project/src
COPY /src /project/src

RUN mkdir -p /project/excel_files
RUN chmod 643 /project/excel_files
RUN export PYTHONPATH="/project"

WORKDIR /project

CMD ["/usr/bin/supervisord"]