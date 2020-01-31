# Pre-requisites

- Couchbase Server 6.5.x
- Python 3.6.x

> Setup your environment as described on Python SDK docs [here](https://docs.couchbase.com/python-sdk/current/start-using-sdk.html)

# Install Python dependencies

```
$ pip install -r requirements.txt
```

# Settings (settings.py file)

Update the settings to your cluster configuration

```
...
# Username of the data user
USERNAME = *****
# Password of the data user
PASSWORD = *****
# Administrator username
ADMIN_USER = *****
# Administrator password
ADMIN_PASS = *****
# The list of nodes
CLUSTER_NODES = ["localhost", "127.0.0.1", *****]
...
```

# Create the dataset 

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

# Start and enjoy!

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

# Cleanup 

> Optional

```
$ python cleanup.py
Cleaning up bucket cbex...
Clean up finished!
```
