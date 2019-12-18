# CouchbasEx

Stock/FX/Cryptocurrencies exchange demo application on Python and Couchbase

## Pre-requisites

- Couchbase Server 6.x
- Python 2.7.x

### MacOS

#### Edit /etc/hosts



Open **/etc/hosts** file as **sudo**:

```
$ sudo open /etc/hosts
```

Add Couchbase Server Cluster IP as cbex-cluster:
```
127.0.0.1 cbex-cluster
```


#### Install brew

```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

> For more info click [here](https://brew.sh/index_es)

#### Install Python 2.7.x

```
$ brew install python@2
```

#### Install Python 2 dependencies

```
$ pip install twisted tornado
```
#### Settings

Please adjust your settings on **settings.py** file

#### Create bucket

Please log to admin console and create bucket *cbex**

#### Create dataset 
```
$ python2 create_dataset.py
```
#### Create index

Login on admin console and create primary index using the following command on query editor:

```
CREATE PRIMARY INDEX on cbex;
```

#### Start and enjoy!

```
$ python2 web-server.py
```




