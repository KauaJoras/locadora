from flask import Blueprint, flash, redirect, render_template, url_for
from app.models import Movie, Game, User

items_bp = Blueprint("items", __name__, url_prefix="/items")

rentals = []

# === FILMES ===
pulp = Movie(1, "Pulp Fiction", "Tarantino")
pulp.image = "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=500&q=80"

her = Movie(2, "Her", "Spike Jonze")
her.image = "https://images.unsplash.com/photo-1517602302552-471fe67acf66?auto=format&fit=crop&w=500&q=80"

blade = Movie(3, "Blade Runner", "Ridley Scott")
blade.image = "https://images.unsplash.com/photo-1516280440614-37939bbacd81?auto=format&fit=crop&w=500&q=80"

# === JOGOS ===
gow = Game(4, "God of War", "PS2")
gow.image = "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=500&q=80"

sotn = Game(5, "Castlevania SOTN", "PS1")
sotn.image = "https://images.unsplash.com/photo-1517649763962-0c623066013b?auto=format&fit=crop&w=500&q=80"

zelda = Game(6, "Zelda Ocarina", "N64")
zelda.image = "https://images.unsplash.com/photo-1513106580091-1d82408b8cd6?auto=format&fit=crop&w=500&q=80"

catalog = [pulp, her, blade, gow, sotn, zelda]
rentals = []


def create_rental(item_id: int):
    item = next((entry for entry in catalog if entry.item_id == item_id), None)
    if item is None or not item.is_available:
        return None

    user = User(1, "Visitante")
    rental = item.rent(user)
    rentals.append(rental)
    return rental


@items_bp.route("/")
def list_items():
    return render_template("items/list.html", items=catalog)


@items_bp.route("/<int:item_id>/rent", methods=["POST"])
def rent_item(item_id):
    rental = create_rental(item_id)
    if rental is None:
        flash("Este item não está disponível no momento.", "danger")
        return redirect(url_for("items.list_items"))

    flash(f"{rental.item.title} alugado com sucesso!", "success")
    return redirect(url_for("rentals.list_rentals"))