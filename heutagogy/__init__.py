from flask import Flask

app = Flask(__name__)

import heutagogy.heutagogy  # noqa
import heutagogy.auth       # noqa
import heutagogy.views      # noqa
