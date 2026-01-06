from flask import Flask
from models import db, User
from flask_migrate import Migrate


app = Flask(__name__)
#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
migrate = Migrate(app, db)
db.init_app(app)








@app.route('/')
def index():
    return f"hello welcome to the server"


if __name__== "__main__":
    app.run(port=5500, debug=True)
