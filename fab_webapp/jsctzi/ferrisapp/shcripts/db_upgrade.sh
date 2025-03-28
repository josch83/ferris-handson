#!/bin/bash

cd /app/ferrisapp
export FLASK_APP=app/__init__.py

flask db upgrade --directory /tmp/migrations