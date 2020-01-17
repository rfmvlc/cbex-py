#!/usr/bin/env - python

import json
import sys

from couchbase.admin import Admin

import settings

# Settings
bucket_name = settings.BUCKET_NAME
user = settings.USERNAME
password = settings.PASSWORD
node = settings.CLUSTER_NODES[0]
admin_user = settings.ADMIN_USER
admin_password = settings.ADMIN_PASS
admin_port = settings.ADMIN_PORT
timeout = settings.TIMEOUT
bucket_ram_quota = settings.BUCKET_RAM_QUOTA


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
            "!!! Error creating the bucket {0}:\n{1}\nExecute cleanup.py and try again".format(bucket_name, sys.exc_info()))


def add_indexes(bucket_manager):
    try:
        bucket_manager.n1ql_index_create_primary(ignore_exists=True)
    except:
        print("!!! Error creating indexes:\n{0}".format(sys.exc_info()))


def add_stocks(sdk_client):
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


if __name__ == '__main__':
    sdk_admin = Admin(admin_user, admin_password, host=node, port=admin_port)
    admin_create_bucket(sdk_admin)
    # sdk_client = Bucket('couchbase://{0}/{1}'.format(node, bucket_name), username=user, password=password)
    # sdk_client.timeout = timeout
    # bucket_manager = sdk_client.bucket_manager();
    # add_stocks(sdk_client)
    # add_indexes(bucket_manager)
