release: env FLASK_APP=heutagogy flask db upgrade
web: gunicorn heutagogy:app
worker: rq worker --url $REDIS_URL
