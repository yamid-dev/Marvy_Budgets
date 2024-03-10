from flask import Flask
from .models import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    bcrypt.init_app(app)

    from .routes import usuario_bp, ingresos_bp, egresos_bp, compras_bp
    app.register_blueprint(usuario_bp)
    app.register_blueprint(ingresos_bp)
    app.register_blueprint(egresos_bp)
    app.register_blueprint(compras_bp)
    
    return app