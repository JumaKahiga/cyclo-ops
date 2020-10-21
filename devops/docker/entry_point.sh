#!/bin/bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

echo "Setting up the database ........."
python -m flask db stamp heads
python -m flask db migrate
python -m flask db upgrade

echo "Database setup successful ........."


gunicorn -w 2 -b 0.0.0.0:5000 --timeout 60 --access-logformat STRING \
--access-logfile - cyclops.unicorn:app
