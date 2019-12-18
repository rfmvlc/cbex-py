# CouchbasEx

Stock/FX/Cryptocurrencies exchange demo application on Python and Couchbase

## Pre-requisites

- Couchbase Server 6.x
- Python 2.7.x

### MacOS/Linux

#### Edit /etc/hosts

```
$ sudo open /etc/hosts
```

Add Couchbase Server Cluster IP as **cbex-cluster**

```
127.0.0.1 cbex-cluster
```

#### Install Python dependencies

```
$ pip install twisted tornado
```

#### Settings (settings.py file)

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

#### Create bucket

Log-in into the admin console and create bucket **cbex**

#### Create dataset 

```
$ python create_dataset.py
```

#### Create index

Login into the admin console and create primary index on **cbex** bucket

```
CREATE PRIMARY INDEX on cbex;
```

#### Start and enjoy!

```
$ python web-server.py
```
