from flask import current_app, Flask, request, session
#Import blueprints here

def create_app() -> Flask:
    app = Flask(__name__)

    #Register blueprints here
    #app.registerblueprint()

    app.before_request(before_request)

    return app

def before_request():
    return