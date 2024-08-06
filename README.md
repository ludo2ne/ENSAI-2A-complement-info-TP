# ENSAI-2A-complement-info-TP

Author : [Rémi Pépin](https://gitlab.com/remi2J/complement_info_ensai_2022_2023), Ludovic Deneuville

## Goals

These practical exercises will be useful as part of the IT project

* TP 1: Back to OOP, business objects and strategy design patterns
* TP 2: Webservices and data formats
* TP 3: Data Access Object (DAO)
* TP 4: Creating an HMI (Human Machine Interface)

## Install

Install the required packages with the following bash commands :

```bash
pip install -r requirements.txt     # install all packages listed in the file
pip list                            # to list all installed packages
```

* **psycopg2-binary** : This package is the PostgreSQL adapter for Python.
* **dataclasses** : The dataclasses module provides a decorator-based approach to creating data classes.
* **python-dotenv** : This library allows you to load environment variables from a .env file.
* **fastapi** : FastAPI is a modern web framework for building APIs with high performance.
* **inquirerPy** : Library that lets you create interactive command-line interfaces with questions and options for users.

## Run

```bash
python src/__main__.py
```