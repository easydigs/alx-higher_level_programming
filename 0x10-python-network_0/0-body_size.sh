#!/bin/bash
# Get the size of the HTTP response header for a given URL.
curl -sI "$1" | wc -c
