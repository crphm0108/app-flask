# app-flask

## installation

```bash
cd /path/to/app-flask
pyenv install 3.7.12 2.7.18
pyenv local 3.7.12
python -m venv .venv
pip install --upgrade pip
pip install --upgrade setuptools
pip install -r requirements.txt
```

## running

```bash
source .venv/bin/activate
python flask run
```

## memo

```bash
pip install flake8 black mypy
pip install Flask
pip install python-dotenv watchdog
pip install pytest pytest-mock
pip install Cerberus
pip install gunicorn ptvsd
```
