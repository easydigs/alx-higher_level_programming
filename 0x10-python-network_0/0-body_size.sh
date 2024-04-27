#!/bin/bash
# Get the size of the HTTP response header for a given URL.
curl -s -I "$1" | grep -i Content-Length | awk '{print $2}'