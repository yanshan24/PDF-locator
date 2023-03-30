PDF-Locator
===================================
# install dependencies
pip install -r requirements.txt
# migrations
python manage.py makemigrations\
python manage.py migrate
# run backend
python manage.py runserver
## admin
http://127.0.0.1:8000/admin \
username: team3\
password: 1234
## API Documentation
http://127.0.0.1:8000/api-docs/
