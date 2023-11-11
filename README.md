# Running Postgres locally

**Start DB**

`docker compose up`

**Stop DB**

Ctrl + C in the terminal if following process

Otherwise, type

`docker compose down`

Can also be stopped via docker desktop UI

# Python

**Initial setup**

First, create then activate a python3 virtual env

```sh
python3 -m venv venv
source venv/bin/activate
```

Then, install dependencies

```sh
pip install -r tools/requirements.txt
```

**Activate existing installation**

```sh
source venv/bin/activate
```
