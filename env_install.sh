#!/bin/bash

echo "Python v.2.7.18 & v.3.7.0 installation in progress ..."
pyenv install 2.7.18 &> /dev/null
pyenv install 3.7.0 &> /dev/null
echo "Done! Virtualenv's creation ..."
pyenv virtualenv 2.7.18 env_python_2.7.18
pyenv virtualenv 3.7.0 env_python_3.7.0
echo "Virtual environments env_python_2.7.18 & env_python_3.7.0 created."
