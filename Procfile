release: env FLASK_APP=heutagogy flask db upgrade
web: gunicorn heutagogy:app
worked: rq worker --url $REDIS_URL
