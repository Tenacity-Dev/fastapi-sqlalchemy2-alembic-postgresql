# FastAPI + SQLAlchemy 2 + Alembic + Postgresql

### The project includes:
- FastAPI
- SQLAlchemy 2
- Alembic
- PostreSQL
- Type Safe Environment Variables
- Feature Based Project Structure like Django's

This is a starter template for creating API's with FastAPI, SQLAlchemy 2, Alembic and Postgresql

The project has env setup. You can view how the config works inside the `/core/config.py` directory, adding new env variables is trivial.

The project is also has a feature based architecture setup for you so that you have a clear idea on how to continue building and adding new features.

## How to use this starter

Clone the repository:
```
git clone https://github.com/Tenacity-Dev/fastapi-sqlalchemy2-alembic-postgresql.git
```

cd into the repository:
```
cd fastapi-sqlalchemy2-alembic-postgresql
```

To make this repository yours:
```
rm -rf .git && git init
git add .
git commit -m "Initial commit"
```

Create a virtual environment with python:
```
python -m venv .venv
# or
python3 -m venv .venv
```

Activate the virtual environment:
```
# For linux or mac
source .venv/bin/activate

# For windows
venv\Scripts\activate
```

Install the requirements:
```
pip install -r requirements.txt
```

Create a .env file and add the required env variables to it (the example of required variables can be seen in .env.local):
```
cp .env.local .env

# Add the required env vars
```

(Optional) Run migrations to create initial user:
```
alembic upgrade head
```

You can also delete the one existing migration and do as you please.

Start the local server:
```
fastapi dev main.py
```
