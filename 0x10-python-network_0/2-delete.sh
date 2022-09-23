#!/bin/bash
# script that sends DELETE request to URL passed as first arg
curl -s "$1" -X DELETE
