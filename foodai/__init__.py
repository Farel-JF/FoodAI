from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from sqlalchemy import create_engine

# Remplace 'username', 'password' et 'db_name' par les bonnes valeurs
engine = create_engine("mysql+pymysql://root:Farel275&@localhost/db")


# Initialize the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Farel275&@localhost/FoodAI'
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
migrate = Migrate(app, db)

# Import routes and models after initialization
from foodai import routes, models

if __name__ == '__main__':
    app.run(debug=True)
