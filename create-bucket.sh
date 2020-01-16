#!/usr/bin/env bash

# ***********************************************************************************************************
# template-simple.sh
#
#   Usage: ./template-simple.sh [options]
#
#   Description and purpose of the script goes here
#
#   Options:
#
#     --cluster     The cluster address (default: cbex-cluster)
#     --username    Cluster Admin or RBAC username (default: Administrator)
#     --password    Cluster Admin or RBAC password (default: password)
#     --port        The port to use (default: 8091)
#     --protocol    The protocol to use (default: http)
#     --bucket      The bucket to use (default: cbex)
# ***********************************************************************************************************

# set the defaults, these can all be overriden as environment variables or passed via the cli
CLUSTER=${CLUSTER:='cbex-cluster'}
USERNAME=${CB_USERNAME:='Administrator'}
PASSWORD=${CB_PASSWORD:='password'}
BUCKET=${CB_BUCKET:='cbex'}
PORT=${PORT:='8091'}
PROTOCOL=${PROTOCOL:='http'}
TIMEOUT=${TIMEOUT:=5}

# parse any cli arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    -c|--cluster) CLUSTER=${2} && shift 2;;
    -r|--port) PORT=${2} && shift 2;;
    -s|--protocol) PROTOCOL=${2} && shift 2;;
    -t|--timeout) TIMEOUT=${2} && shift 2;;
    -b|--bucket) BUCKET=${2} && shift 2;;
    -u|--username) USERNAME=${2} && shift 2;;
    -p|--password)
      # if no password was specified prompt for one
      if [[ "${2:-}" == "" || "${2:-}" == --* ]]; then
        stty -echo # disable keyboard input
        read -p "Password: " -r PASSWORD # prompt the user for the password
        stty echo # enable keyboard input
        echo # new line
        tput cuu1 && tput el # clear the previous line
        shift
      else
        # shellcheck disable=SC2034
        PASSWORD="${2}" # set the passed password
        shift 2
      fi
      ;;
    *)
      error "invalid option: '$1'."
      exit 1
      ;;
  esac
done

# make sure jq exists
if [ "$(command -v jq)" = "" ]; then
  echo >&2 "jq command is required, see (https://stedolan.github.io/jq/download)";
  exit 1;
fi

# main script logic goes here
# get the index stats for the bucket
curl \
  --user "$USERNAME:$CB_PASSWORD" \
  --request POST \
  --silent \
  "$PROTOCOL://$CLUSTER:$PORT/pools/default/buckets"
