from flask import Flask

app = Flask(__name__)

from app.blueprints.main import bp as main_bp
app.register_blueprint(main_bp)