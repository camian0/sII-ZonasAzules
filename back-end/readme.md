# Fast api backend

Project to handle backend for project of blue zones into city

## Setup environment

We are located in the root folder of the backend

1- Create virtual environment

```bash
 python -m venv .venv
```

2- Activate virtual environment

```bash
  ./.venv/Scripts/activate
```

## Setup libraries

We should be sure of activate virtual enviroment

Install packages

```bash
    pip install <nombre-paquete>
```

Update libraries into requirements file:

```bash
    Linux pip freeze > requirements.txt

    Windows pip freeze > .\requirements.txt

```

Install dependencies from requirements file

```bash
    Windows: pip install -r .\requirements.txt

    Linux: pip install -r requirements.txt
```

## Setup alembic

1. Create a copy of file alembic-example.ini and change name for alembic.ini

```bash
    python ./config/setupAlembicEngine.py
```

2 You need run configuration setup file, and take them to data base params into alembic.ini file, these data load from environment variables(.env file)

```bash
    python ./config/setupAlembicEngine.py
```
