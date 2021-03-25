from flask import Flask

def getApp(app = None) :
    if app is None :
        app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_DAVIDVISITORS')
    # app.secret_key = os.environ.get('SECRET_KEY_DAVIDVISITORS')
    # app.config['PERMANENT_SESSION_LIFETIME'] = 3600
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app