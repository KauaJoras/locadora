from flask import Blueprint, flash, redirect, render_template, url_for
from app.models import Movie, Game, User

items_bp = Blueprint("items", __name__, url_prefix="/items")

rentals = []

# === FILMES ===
front_url = "/static/images/pulp-fiction-front.jpg"
side_url = "/static/images/pulp-fiction-side.jpg"
back_url = "/static/images/pulp-fiction-back.jpg"

pulp = Movie(1, "Pulp Fiction", "Tarantino")
pulp.image = front_url
pulp.front_image = front_url
pulp.side_image = side_url
pulp.back_image = back_url

her = Movie(2, "Her", "Spike Jonze")
her.image = front_url
her.front_image = front_url
her.side_image = side_url
her.back_image = back_url

blade = Movie(3, "Blade Runner", "Ridley Scott")
blade.image = front_url
blade.front_image = front_url
blade.side_image = side_url
blade.back_image = back_url

# === JOGOS ===
gow = Game(4, "God of War", "PS2")
gow.image = front_url
gow.front_image = front_url
gow.side_image = side_url
gow.back_image = back_url

sotn = Game(5, "Castlevania SOTN", "PS1")
sotn.image = front_url
sotn.front_image = front_url
sotn.side_image = side_url
sotn.back_image = back_url

zelda = Game(6, "Zelda Ocarina", "N64")
zelda.image = front_url
zelda.front_image = front_url
zelda.side_image = side_url
zelda.back_image = back_url

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