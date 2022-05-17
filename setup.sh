# Python 3 is required, I used 3.10.4
python3 --version
# Pip for python 3 is required, I used 22.0.2
pip --version
# Without other containers used, venv is recommended
# to not mesh dependencies when swapping projects
python3 -m venv venv
# Activate venv
. venv/bin/activate

# Installing Django and other requirements
python -m pip install Django
# Check the version used, I had 4.0.4
django-admin --version

# Install Django REST framework
python -m pip install djangorestframework

# Deactivate venv after everything is done
deactivate
