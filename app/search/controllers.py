# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import the database object from the main app module
from app import db

from app.api.models import Urls,Pods
from app.api.models import dm_dict_en
from app.search import score_pages


# Define the blueprint:
search = Blueprint('search', __name__, url_prefix='')

@search.route('/')
@search.route('/index')
def index():
    results = []
    query = request.args.get('q')
    print(request,request.args,query)
    num_entries = len(Urls.query.all())
    me = Pods.query.all()[0]
    if not query:
        return render_template("search/index.html", num_entries=num_entries, name=me.name, description=me.description)
    else:
        results = []
        query = query.lower()
        pears = ['0.0.0.0']
        results = score_pages.run(query, pears)
        return render_template('search/results.html', pears=pears,
                               query=query, results=results, num_entries=num_entries, name=me.name, description=me.description)


