# Bookshop Management System

Software Requirements:
Python 3.6
pip 21.x
postgresql 12.6

Clone and Setup the environment:
git clone git@github.com:scaleworxx/bookshop_management_system.git
cd bookshop_management_system
sudo pip3 install virtualenv
virtualenv -p python3.6 scaleworxx-venv
source scaleworxx-venv/bin/activate
pip install -r requirements.txt


Database setup:
sudo -u postgres psql
CREATE DATABASE scaleworxx_dev;
CREATE USER scaleworxx_user WITH ENCRYPTED PASSWORD 'scaleworxx';
ALTER ROLE scaleworxx_user SET client_encoding TO 'utf8';
ALTER ROLE scaleworxx_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE scaleworxx_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE scaleworxx_dev TO scaleworxx_user;
