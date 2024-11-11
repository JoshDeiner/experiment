from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import and register blueprints
    from app.controllers.home_controller import home_bp
    app.register_blueprint(home_bp)

    return app
