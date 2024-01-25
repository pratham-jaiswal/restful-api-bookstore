from flask import Flask
from app.config import Config
from app.models import mongo, bcrypt
from app.routes import main

app = Flask(__name__)
app.config.from_object(Config)

mongo.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)