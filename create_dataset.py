#!/usr/bin/env - python

import json
import sys
import time

import requests
from couchbase.admin import Admin
from couchbase.bucket import Bucket
from requests.auth import HTTPDigestAuth, HTTPBasicAuth

import settings

# Settings
bucket_name = settings.BUCKET_NAME
user = settings.USERNAME
password = settings.PASSWORD
node = settings.CLUSTER_NODES[0]
admin_user = settings.ADMIN_USER
admin_password = settings.ADMIN_PASS
timeout = settings.TIMEOUT
bucket_ram_quota = settings.BUCKET_RAM_QUOTA
fts_index_name = settings.FTS_INDEX_NAME


def admin_create_bucket(sdk_admin):
    # print(sdk_admin.bucket_info(name=bucket_name))
    try:
        print("Creating bucket {0}...".format(bucket_name))
        sdk_admin.bucket_create(name=bucket_name, bucket_type='couchbase', flush_enabled=True,
                                ram_quota=bucket_ram_quota)
        print("Waiting for bucket {0} to be available...".format(bucket_name))
        sdk_admin.wait_ready(bucket_name, timeout=timeout)
    except:
        print(
            "!!! Error creating the bucket {0}:\n{1}\nExecute cleanup.py and try again".format(bucket_name,
                                                                                               sys.exc_info()))


def add_indexes(bucket_manager):
    try:
        print("Creating primary index on {0}...".format(bucket_name))
        bucket_manager.n1ql_index_create_primary(ignore_exists=True)
        print("Indexes created successfully!")
    except:
        print("!!! Error creating indexes:\n{0}\nExecute cleanup.py and try again".format(sys.exc_info()))


def add_stocks(sdk_client):
    print("Loading dataset...")
    # https://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download
    stocks_json = open(settings.STOCKS_FILE, 'r')
    stocks_dict = json.load(stocks_json)
    symbol_list = []
    stock_count = 0
    for stock_doc in stocks_dict:
        if stock_count >= settings.NUM_STOCKS:
            break
        if 'priority' not in stock_doc:
            stock_doc['priority'] = 2
        stock_key = "stock:" + stock_doc['symbol']
        symbol_list.append(stock_key)
        sdk_client.upsert(stock_key, stock_doc)
        stock_count += 1
    sdk_client.upsert(settings.PRODUCT_LIST, {"symbols": symbol_list})
    print("Successfully populated dataset!")


def add_fts_indexes():
    print("Creating fts index {0} on {1}...".format(fts_index_name, bucket_name))
    fts_json = open(settings.FTS_INDEX_FILE, 'r')
    url = "http://{0}:8094/api/index/{1}".format(node, fts_index_name)
    payload = json.load(fts_json)
    headers = {'content-type': 'appllication.json'}
    x = requests.put(url, data=json.dumps(payload), headers=headers, timeout=timeout, auth=HTTPBasicAuth(admin_user, admin_password))
    if x.status_code == 200:
        print("Indexes created successfully!")
    else:
        print("!!! Error creating indexes:\n{0}\nExecute cleanup.py and try again".format(x.text))



if __name__ == '__main__':
    sdk_admin = Admin(admin_user, admin_password, host=node)
    admin_create_bucket(sdk_admin)
    # Workaround wait_ready is not enough...
    time.sleep(timeout)
    sdk_client = Bucket('couchbase://{0}/{1}'.format(node, bucket_name), username=user, password=password)
    sdk_client.timeout = timeout
    bucket_manager = sdk_client.bucket_manager();
    add_stocks(sdk_client)
    add_indexes(bucket_manager)
    add_fts_indexes()

