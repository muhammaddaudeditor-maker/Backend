#!/bin/bash

echo "BUILD START"
python3.12 -m pip install -r requirements.txt

# Remove old staticfiles to avoid conflicts
rm -rf staticfiles

# Collect static files
python3.12 manage.py collectstatic --noinput --clear

echo "BUILD END"