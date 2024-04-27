from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ssecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

from routes import *

if __name__ =='__main__':
    with app.app_context():         # <--- without these two lines, 
        db.create_all()             # <--- we get the OperationalError in the title
        app.run(debug=True)