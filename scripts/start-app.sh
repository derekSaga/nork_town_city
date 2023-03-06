#!/bin/bash

set -e

flask db upgrade

python main.py