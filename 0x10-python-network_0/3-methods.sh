#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.
curl -s -I "$1" | grep Allow | cut -d " " -f 2-
