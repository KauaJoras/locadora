from flask import Blueprint, render_template
from app.models import Movie, Game

items_bp = Blueprint("items", __name__, url_prefix="/items")

catalog = [
    Movie(1, "Matrix", "Wachowski"),
    Game(2, "God of War", "PS5"),
    Movie(3, "Inception", "Nolan"),
]

@items_bp.route("/")
def list_items():
    return render_template("items/list.html", items=catalog)