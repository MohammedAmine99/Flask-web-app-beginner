from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your own secret key

    # Import and register blueprints here
    from .views import main_blueprint
    app.register_blueprint(main_blueprint)

    return app