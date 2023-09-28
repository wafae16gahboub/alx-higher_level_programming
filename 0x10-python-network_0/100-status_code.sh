#!/bin/bash
# Sends a GET request
curl -s -o /dev/null -w "%{http_code}" "$1"
