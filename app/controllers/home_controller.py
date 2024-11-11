from flask import Blueprint, render_template
from app.models.item import Item

home_bp = Blueprint('home', __name__)

@home_bp.route("/")
def home():
    # Example: Pass data to the view
    sample_item = Item("Flask MVC", "A sample MVC structured application.")
    return render_template("home.html", item=sample_item)
