# FastAPI + SQLAlchemy 2 + Alembic + Postgresql

This is a starter template for creating API's with FastAPI, SQLAlchemy 2, Alembic and Postgresql

The project has env setup. You can view how the config works inside the `/core/config.py` directory, adding new env variables is trivial.

The project is also has a feature based architecture setup for you so that you have a clear idea on how to continue building and adding new features.

## How to use this starter

---
Clone the repository:
```
https://github.com/Tenacity-Dev/fastapi-sqlalchemy2-alembic-postgresql.git
```

cd into the repository:
```
cd fastapi-sqlalchemy2-alembic-postgresql
```

To make this repository yours:
```
rm -rf .git && git init && npm init
git add .
git commit -m "Initial commit"
```

Create a virtual environment with python:
```
python -m venv .venv
# or
python3 -m venv .venv
```

Install the requirements
```
pip install -r requirements.txt
```

Start the local server:
```
fastapi dev main.py
```
