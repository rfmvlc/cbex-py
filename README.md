# CBEX

Stock/Crypto-currencies exchange demo application
===

## Pre-requisites

- Couchbase Server 6.x
- Python 3.x

## Install Python dependencies

```
$ pip install -r requirements.txt
```

## Settings (settings.py file)

Update the settings to your cluster configuration

```
...
# Username of the data user
USERNAME = "Your User"
# Password of the data user
PASSWORD = "Your Password"
# Administrator username
ADMIN_USER = "Administrator User"
# Administrator password
ADMIN_PASS = "Administrator Password"
...
```

## Create dataset 

```
$ python create_dataset.py
```

## Create indexes

Login into the admin console and create primary index on **cbex** bucket

```
CREATE PRIMARY INDEX on cbex;
```

## Start and enjoy!

```
$ python app.py
...
Running at http://localhost:8888
Live Prices WebSocket opened
CB Status WebSocket opened
```
