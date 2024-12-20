from flask import Flask

from app.apis import RECAPTCHA_PRIVATE_KEY,RECAPTCHA_PUBLIC_KEY

from flask_wtf.csrf import CSRFProtect
from flask_wtf import RecaptchaField
from app.Config import Config
from app.apis import RECAPTCHA_PRIVATE_KEY,RECAPTCHA_PUBLIC_KEY
#csrf = None 


def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)
    app.config.from_object(Config)

    app.secret_key = 'your_secret_key'

    app.config['DEBUG'] = True
    app.config['UPLOAD_FOLDER'] =Config.UPLOAD_FOLDER
    app.config['retyculated_databases']=Config.RETICULATED_FOLDER
    app.config["RECAPTCHA_PUBLIC_KEY"]=RECAPTCHA_PUBLIC_KEY
    app.config["RECAPTCHA_PRIVATE_KEY"]=RECAPTCHA_PRIVATE_KEY
    from app.routes import create_database_routes,create_routes,dawnload_routes,getkey_routes,getschema_routes,home_routes,querywkey_routes
    app.register_blueprint(create_database_routes.bp)
    app.register_blueprint(create_routes.bp)
    app.register_blueprint(dawnload_routes.bp)
    app.register_blueprint(getkey_routes.bp)
    app.register_blueprint(getschema_routes.bp)
    app.register_blueprint(home_routes.bp)
    app.register_blueprint(querywkey_routes.bp)
    csrf.exempt(getkey_routes.bp)
    csrf.exempt(create_routes.bp)
    csrf.exempt(dawnload_routes.bp)
    csrf.exempt(getkey_routes.bp)
    csrf.exempt(getschema_routes.bp)
    csrf.exempt(home_routes.bp)
    csrf.exempt(querywkey_routes.bp)

    recaptcha=RecaptchaField()
    return app
   
    
