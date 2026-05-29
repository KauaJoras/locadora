from flask import Flask, redirect, url_for
import os

def create_app():
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
    app = Flask(__name__, template_folder=template_dir)

    from app.routes.items import items_bp
    from app.routes.rentals import rentals_bp
    app.register_blueprint(items_bp)
    app.register_blueprint(rentals_bp)

    @app.route("/")
    def index():
        return redirect(url_for("items.list_items"))

    return app