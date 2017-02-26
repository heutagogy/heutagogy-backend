from flask import Flask

app = Flask(__name__)

from heutagogy.heutagogy import db # noqa
import heutagogy.persistence       # noqa
import heutagogy.views             # noqa
import heutagogy.auth              # noqa
import heutagogy.acme              # noqa
