#!/bin/bash
set -o errexit

gunicorn config.wsgi:application --bind 0.0.0.0:8000