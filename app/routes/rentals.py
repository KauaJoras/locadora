from flask import Blueprint, redirect, render_template, url_for
from app.routes.items import rentals

rentals_bp = Blueprint("rentals", __name__, url_prefix="/rentals")


@rentals_bp.route("/")
def list_rentals():
    return render_template("rentals/list.html", rentals=rentals)


@rentals_bp.route("/<int:rental_index>/return", methods=["POST"])
def return_rental(rental_index):
    if 0 <= rental_index < len(rentals):
        rental = rentals[rental_index]
        rental.return_item()
        rentals.pop(rental_index)
    return redirect(url_for("rentals.list_rentals"))
