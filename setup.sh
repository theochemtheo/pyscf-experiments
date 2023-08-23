#!/usr/bin/env bash

# check we're in a venv
if [[ "$VIRTUAL_ENV" = "" ]]; then
  echo "Not running in a python virtualenv, please create a venv and rerun:"
  echo
  echo "  > python -m venv .venv"
  echo "  > source .venv/bin/activate"
  echo "  > ./setup.sh"
  exit 1
fi

# check python version
if ! [[ "$(python -V)" == *"3.11."* ]]; then
  echo "Python version >= 3.11 required"
  exit 1
fi

# upgrade then run pip
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
