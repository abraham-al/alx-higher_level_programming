#!/bin/bash
# displays only the status code of the response
curl -s "$1" -o /dev/null -w "%{http_code}"
