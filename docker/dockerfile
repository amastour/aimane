FROM ubuntu:20.04 AS compile-image

# install apt packages
RUN apt update 
RUN apt install -y python3 python3-pip  python3-dev python3-venv

# prepare python environement
COPY src/requirements.txt /opt/requirements.txt
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip3 install uwsgi==2.0.18
RUN pip3 install -r /opt/requirements.txt




FROM ubuntu:20.04 AS runtime-image

# install apt package
RUN apt update 
RUN apt install -y python3 libpython3.8-dev

# prepare uwsgi folder
RUN mkdir -p /opt/uwsgi
ADD docker/uwsgi.ini /opt/uwsgi/
ADD docker/startserver.sh /opt/uwsgi/

# create user uwsgi
RUN adduser --no-create-home --disabled-password --shell /bin/sh uwsgi
USER uwsgi

# get virtualenv from compile image
COPY --chown=uwsgi:uwsgi --from=compile-image /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
# get code project
ADD --chown=uwsgi:uwsgi src/ /opt/code
# prepare to execute
WORKDIR /opt/code
EXPOSE 5000
ENV CONFIG_TYPE=dev
RUN python3 /opt/code/manage.py db_init

CMD ["/bin/sh", "/opt/uwsgi/startserver.sh"]
