# for-hublo

## About 

Just a SQL join implementation in vanilla Python.

## Usage

### Install

In your terminal, run the following command:

```bash
poetry install
```

### Run

In your terminal, run the following command:

```bash
poetry run python -m pytest .
```

## Structure 
```
├── CHANGELOG.md    : Changelog file
├── LICENSE         
├── poetry.lock     
├── pyproject.toml  : Poetry project file
├── README.md       
├── src             : Source code
│   ├── __init__.py
│   ├── sql.py      : Main Sql class
│   └── vars.py     : Variables file
└── tests
    ├── __init__.py
    └── test_sql.py : Test file
```