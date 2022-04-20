#!/usr/bin/env bash

pip uninstall torbjorn -y

python setup.py clean
python setup.py install
