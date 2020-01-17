#!/usr/bin/env - python

from couchbase.bucket import Bucket
from couchbase.admin import Admin
import settings
import random
import json

# Settings
bucket_name = settings.BUCKET_NAME
user = settings.USERNAME
password = settings.PASSWORD
node = settings.CLUSTER_NODES[0]
admin_user = settings.ADMIN_USER
admin_password = settings.ADMIN_PASS
admin_port = settings.ADMIN_PORT

# Global SDK


def admin_create_bucket(sdk_admin):
    sdk_admin.bucket_create(name=bucket_name, bucket_type='couchbase',flush_enabled=True)


def sdk_client_init():



def check_and_create_view():
    design_doc = {
        'views': {
            'by_timestamp': {
                'map': '''
                function(doc, meta) {
                    if (doc.type && doc.type== "order" && doc.ts) {
                        emit(doc.ts, null)
                    }
                    }
                '''
            }
        }
    }

    mgr = SDK_CLIENT.bucket_manager()
    mgr.design_create(settings.DDOC_NAME, design_doc, use_devmode=False)
    res = SDK_CLIENT.query(settings.DDOC_NAME, settings.VIEW_NAME)
    for row in res:
        print(row)


def add_stocks():
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
        SDK_CLIENT.upsert(stock_key, stock_doc)
        stock_count += 1
    SDK_CLIENT.upsert(settings.PRODUCT_LIST, {"symbols": symbol_list})


if __name__ == '__main__':
    sdk_admin = Admin(admin_user, admin_password, host=node, port=admin_port)
    admin_create_bucket(sdk_admin)
    sdk_client = Bucket('couchbase://{0}/{1}'.format(node, bucket_name), username=user, password=password)
    SDK_CLIENT.timeout = 15
#    sdk_client_init()
#    add_stocks()
#    check_and_create_view()
    print("Successfully populated dataset")
