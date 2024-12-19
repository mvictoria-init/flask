from flask import Flask, render_template, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
from decouple import config


# create the extension
db = SQLAlchemy()

def create_app():
    
    app = Flask(__name__)
    
    # configuracion del proyecto
    app.config.from_mapping(
        SECRET_KEY = config('SECRET_KEY'),
        # create the db
        SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
    )
    
    # initialize the app with the extension
    db.init_app(app)
    
    # registrar Bluprint
    # registrar Bluprint de book
    from . import book
    app.register_blueprint(book.bp)
    # registrar Bluprint de auth
    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/lista_de_libros')
    def index():
        print('here')
        if g.user:
            return redirect(url_for('book.index'))
        return render_template('index.html')
    
    # # migrate all elements
    with app.app_context():
        db.create_all()

    return app