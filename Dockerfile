FROM python:3.6.5

# Setting time zone
ENV TZ="Asia/Tokyo"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# OS Updates 
RUN ["apt-get", "update"]

# Install vim, git
RUN ["apt-get", "install", "-y", "vim"]
RUN ["apt-get", "install", "-y", "git"]

# Install Node.js
# and update
RUN apt-get install --yes curl
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install --yes nodejs
RUN apt-get install --yes build-essential
RUN npm i -g npm

# Install Vue.js
RUN npm install --quiet --global \
      @vue/cli
# RUN npm install --save vue-router
# RUN npm install --save axios 

# Install npm
#RUN npm install http-server -g
#RUN npm install && npm install node-sass && npm run build

# Install pip
# Make code directory
RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip

# Install venv
ADD . /code/

RUN python -m venv django_sample_env
RUN /bin/bash -c "source /code/django_sample_env/bin/activate"
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# PostgreSQL
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
  apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN apt-get update && apt-get install -y software-properties-common postgresql-10 postgresql-client-10 postgresql-contrib-10
USER postgres
RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER adminuser WITH SUPERUSER PASSWORD 'admin2018';" &&\
    createdb -O adminuser adminuser &&\
    createdb -O adminuser django_sample

COPY pg_hba.conf /etc/postgresql/10/main/
RUN echo "listen_addresses='*'" >> /etc/postgresql/10/main/postgresql.conf
EXPOSE 5432
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
CMD ["/usr/lib/postgresql/10/bin/postgres", "-D", "/var/lib/postgresql/10/main", "-c", "config_file=/etc/postgresql/10/main/postgresql.conf"]
RUN service postgresql start

WORKDIR /code

# CMD http-server -p 8080 ./dist