from flask import Blueprint, render_template

rentals_bp = Blueprint("rentals", __name__, url_prefix="/rentals")

@rentals_bp.route("/")
def list_rentals():
    return render_template("rentals/list.html", rentals=[])
