# PF Project
### Alex Jarvis

Small project completed as part of an application for the [Packform](https://www.packform.io/) internship

## Dependencies
```
Postgresql 12.3
Mongo 4.2.8
Python 3.8.3
npm 6.14.5
```

## Development Setup

Below are the steps required to get the project up and running.

Before running the database script you need to write an env file in the following format:
```
DBNAME=db_name
DBUSER=db_user
```
with your postgresql details.

Once that is created you can run the following commands to get the project installed

```
<!-- Flask Backend -->
python3 -m venv venv
source venv/bin/activate
pip install -r requirements

<!-- Vue Front -->
cd packform-vue
npm install

<!-- Databases -->
cd ..
python db_scripts/export.py
```

## Running

Below are the commands to get the project running
```
source venv/bin/activate
FLASK_APP=packform_back/app.py flask run
<!-- Vue front run in seperate terminal -->
cd packform-vue
npm run serve
```
