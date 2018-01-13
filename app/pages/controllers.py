# Import flask dependencies
from flask import Blueprint, render_template

from app.api.models import Pods

# Define the blueprint:
pages = Blueprint('pages', __name__, url_prefix='/pages')

@pages.route('/about/')
def return_about():
    me = Pods.query.all()[0]
    return render_template("pages/about.html", name=me.name)
