python -m venv venv
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

docker pull postgres
docker run -itd -e POSTGRES_PASSWORD=123456 -p 5432:5432  -v /usr/local/docker/pgdata:/var/lib/postgresql/data --name dragonpgdb postgres
