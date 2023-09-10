from flask import Flask
from flask_cors import CORS
from .models.data import db
from .endpoints.api import api_blueprint
from .utils.db_utils import insert_sectors_and_subsectors, clear_tables
from .config import (
    POSTGRES_HOST,
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

app.register_blueprint(api_blueprint, url_prefix='/api')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        clear_tables()
        insert_sectors_and_subsectors()
    app.run(host="0.0.0.0", port=8005)
