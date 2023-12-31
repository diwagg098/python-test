from flask import Flask
from flask_migrate import Migrate
from config import configuration, http
from config.database import db
import os

app = http.create_app(configuration.Configuration)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')

db.init_app(app)
migrate = Migrate(app, db)

port = int(configuration.Configuration.PORT)
if __name__ == "__main__":
     app.run(host="0.0.0.0", port=port, debug=True)
set