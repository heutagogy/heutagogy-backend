from flask import Flask
app = Flask(__name__)

import heutagogy.heutagogy
import heutagogy.auth
import heutagogy.views
