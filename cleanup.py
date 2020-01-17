#!/usr/bin/env - python

from couchbase.admin import Admin

import settings

# Settings
bucket_name = settings.BUCKET_NAME
node = settings.CLUSTER_NODES[0]
admin_user = settings.ADMIN_USER
admin_password = settings.ADMIN_PASS
timeout = settings.TIMEOUT

if __name__ == '__main__':
    sdk_admin = Admin(admin_user, admin_password, host=node)
    print("Cleaning up bucket {0}...".format(bucket_name))
    sdk_admin.bucket_remove(bucket_name)
    print("Clean up finished!")
