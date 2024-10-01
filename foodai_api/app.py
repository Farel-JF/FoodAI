from flask import Flask
from models import db
from config import Config
from routes import app as routes_app

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

app.register_blueprint(routes_app)

if __name__ == "__main__":
    app.run(debug=True)
