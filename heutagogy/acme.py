from heutagogy import app

if app.config['ACME_CHALLENGE']:
    @app.route('/.well-known/acme-challenge/' + app.config['ACME_CHALLENGE'])
    def get_acme():
        return app.config['ACME_RESPONSE']
