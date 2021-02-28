import requests
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class newCG(db.Model):
    id = Column(db.Integer, primary_key=True)
    cgName = db.Column(db.String(400), nullable=False)
    cgDescription = db.Column(db.String(3200), nullable=False)

    def __repr__(self):
        return f"{self.cgName} - {self.cgDescription}"


@app.route('/')
def index():
    return 'Elite Community Goal API Coming Soon'


@app.route('/events')
def events():
    return 'A dictionary of events'


if __name__ == "__main__":
     app.run(debug=True, host="0.0.0.0")


