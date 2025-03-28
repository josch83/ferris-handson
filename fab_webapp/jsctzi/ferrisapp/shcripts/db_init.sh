#!/bin/bash

cd /app/ferrisapp
export FLASK_APP=app/__init__.py

flask db init --directory /tmp/migrations