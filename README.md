# stock-exchange
CB Demo With a Stock Exchange Theme pgraded for 

## Pre-requisites
Couchbase Server 6.x

### MacOS

#### Install brew

```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

> For more info click [here](https://brew.sh/index_es)

#### Install Python 2

```
$ brew install python@2
```

#### Install Python 2 dependencies

```
$ pip install twisted tornado
```
#### Settings

Please adjust your settings on *settings.py* file

#### Create bucket

Please log to admin console and create bucket *cbse*

#### Create dataset 
```
$ python2 create_dataset.py
```
#### Create index

Login on admin console and create primary index using the following command on query editor:

```
CREATE PRIMARY INDEX on cbse;
```

#### Start and enjoy!

```
$ python2 web-server.py
```




