from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '566a11d037b905cca454e08e108a8867'

from credit_scoring import routes