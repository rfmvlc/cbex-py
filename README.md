# CBEX

Stock/Crypto-currencies exchange demo application
===

## Pre-requisites

- Couchbase Server 6.5.x
- Python 3.6.x

> Setup your environment as described on Pyhton SDK docs [here](https://docs.couchbase.com/python-sdk/current/start-using-sdk.html)

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
Creating bucket cbex...
Waiting for bucket cbex to be available...
Loading dataset...
Successfully populated dataset!
Creating primary index on cbex...
Indexes created successfully!
Creating fts index cbex on cbex...
Indexes created successfully!
```

## Start and enjoy!

```
$ python app.py
...
Running at http://localhost:8888
Live Prices WebSocket opened
CB Status WebSocket opened
...
CB Status received: Exchange Node Status Socket Connected
('New Order: ', 'Couchbaser!', 1580323582)
```

## Cleanup 

> Optional: Just in case of error on creation or environment delete

```
$ python cleanup.py
Cleaning up bucket cbex...
Clean up finished!
```

