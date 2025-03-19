#!/bin/bash
echo "BEFORE: ls -l /usr/lib/x86..."
ls -l /usr/lib/x86_64-linux-gnu
sudo apt-get update
sudo apt-get install libmtdev1t64
echo "AFTER: ls -l /usr/lib/x86..."
ls -l /usr/lib/x86_64-linux-gnu
export KIVY_HOME=/home/runner/work/tests_mymodule/tests_mymodule
export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
pipenv install kivy
pipenv install pytest
pipenv run python -m pytest >> ./run-pytest-log.txt
cat ./pytest-log.txt