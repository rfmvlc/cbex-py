# stock-exchange
CB Demo With a Stock Exchange Theme

## Release notes 1.1
- Upgraded for Couchbase Server 6.x

## Pre-requisites

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

- Log in to your admin console and create the index using the following command:

```
CREATE PRIMARY INDEX on cbse;
```

#### Start and enjoy!

```
$ python2 web-server.py
```




