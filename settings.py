# Bucket name
BUCKET_NAME = "cbex"
# FTS index
FTS_INDEX_FILE = "fts_index.json"
# FTS index name
FTS_INDEX_NAME = "cbex"
# Stock file model
STOCKS_FILE = "stocks.json"
# The list of nodes
CLUSTER_NODES = ["localhost"]
# Exposed web port e.g. 8888 or 80
WEB_PORT = 8888
# Whether the current cluster is on AWS
AWS = False
# Username of the data user
USERNAME = "Administrator"
# Password of the data user
PASSWORD = "password"
# Administrator username
ADMIN_USER = "Administrator"
# Administrator password
ADMIN_PASS = "password"
# Name of the design doc
DDOC_NAME = "orders"
# Name of the view
VIEW_NAME = "by_timestamp"
# Doc containing all stocks. 
# Single field called "symbols" which is a list containing all product keys.
PRODUCT_LIST = "stock_list"
# How many stocks should we use?
NUM_STOCKS = 200
# Flavor: stocks/crytoc
FLAVOR = "stocks"
# Default timeout (5s)
TIMEOUT = 5
# Default RAM Quota
BUCKET_RAM_QUOTA = 1024
