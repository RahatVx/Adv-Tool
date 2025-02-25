#!/bin/bash

# Clean temporary files older than 24 hours
find /app/storage/temp -type f -mtime +1 -exec rm -f {} \;
find /app/storage/uploads -type f -mtime +1 -exec rm -f {} \;
