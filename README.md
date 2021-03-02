# Bookshop Management System

### Software Requirements:
##### Host: Ubuntu
1. **Python** 3.6
2. **pip** 21.x
3. **postgresql** 12.6
4. **virtualenv** 20.2.2

##### Host: Docker
1. **Docker** version 20.10.3, build 48d30b5
2. **docker-compose** version 1.18.0, build 8dd22a9


### Database setup:
```
sudo -u postgres psql
CREATE DATABASE scaleworxx_dev;
CREATE USER scaleworxx_user WITH ENCRYPTED PASSWORD 'scaleworxx';
ALTER ROLE scaleworxx_user SET client_encoding TO 'utf8';
ALTER ROLE scaleworxx_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE scaleworxx_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE scaleworxx_dev TO scaleworxx_user;
```


### Clone and Setup the environment:
```
git clone git@github.com:scaleworxx/bookshop_management_system.git
cd bookshop_management_system
```

#### Option1:

```
sudo pip3 install virtualenv
virtualenv -p python3.6 scaleworxx-venv
source scaleworxx-venv/bin/activate
pip install -r requirements.txt
```

#### Option2:

```
docker-compose -f docker-compose-dev.yml build
docker-compose -f docker-compose-dev.yml up -d
```