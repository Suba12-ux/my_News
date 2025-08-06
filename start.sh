#!/bin/bash
set -o errexit

gunicorn news_app.wsgi:application --bind 0.0.0.0:8000