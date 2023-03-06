#!/bin/bash

set -e

flask db upgrade

gunicorn --bind 0.0.0.0:${WEB_PORT} wsgi:app