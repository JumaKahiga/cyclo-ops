#!/bin/bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

echo "Setting up the database ........."
python -m flask db stamp heads
python -m flask db migrate
python -m flask db upgrade

echo "Database setup successful ........."


gunicorn -b 0.0.0.0:5000 -w 2 --timeout 60 cyclops.unicorn:app
