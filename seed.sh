#!/bin/bash
rm -rf levelupapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations artist_collective_ink_serverapi
python3 manage.py migrate artist_collective_ink_serverapi
python3 manage.py loaddata users
python3 manage.py loaddata shops
python3 manage.py loaddata artists
python3 manage.py loaddata styles
python3 manage.py loaddata artist_styles
