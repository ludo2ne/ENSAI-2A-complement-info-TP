# ENSAI-2A-complement-info-TP

Source code for the practical exercises of the ENSAI course [Compléments d'informatique](https://ludo2ne.github.io/ENSAI-2A-Projet-info/).

Authors : [Rémi Pépin](https://gitlab.com/remi2J/complement_info_ensai_2022_2023), Ludovic Deneuville

## Goals

These practical exercises will be useful as part of the IT project

- TP 1: Git usage
- TP 2: Back to OOP, business objects and strategy design patterns
- TP 3: Webservices and data formats
- TP 4: Data Access Object (DAO)

## Install

Install the required packages with the following bash commands :

```bash
pip install -r requirements.txt     # install all packages listed in the file
pip list                            # to list all installed packages
```

- **dataclasses** : The dataclasses module provides a decorator-based approach to creating data classes.
- **fastapi** : FastAPI is a modern web framework for building APIs with high performance.
- **inquirerPy** : Library that lets you create interactive command-line interfaces with questions and options for users.
- **psycopg2-binary** : This package is the PostgreSQL adapter for Python.
- **pytest** : powerful testing framework for Python.
- **python-dotenv** : This library allows you to load environment variables from a .env file.
- **requests** : designed to make HTTP requests easier and more human-friendly.
- **tabulate** : simple way to pretty-print tabular data in Python.
- **uvicorn** : Uvicorn is a lightning-fast ASGI server implementation.


## Unit Tests

```bash
python -m pytest -v
```

## Run

```bash
python src/__main__.py
```