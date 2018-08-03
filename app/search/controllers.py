# Import flask dependencies
from flask import Blueprint, request, render_template, send_from_directory

# Import the database object from the main app module
from app.api.models import Urls,Pods
from app.search import score_pages

# Import utilities
import re

# Define the blueprint:
search = Blueprint('search', __name__, url_prefix='')


def get_cached_urls(urls):
    urls_with_cache = urls
    for u in urls_with_cache:
        cache = re.sub(r"http\:\/\/|https\:\/\/", "", u[0])
        if cache[-5:] != ".html":
            cache += ".html"
        print(cache)
        u.append(cache)
    return urls_with_cache


@search.route('/')
@search.route('/index')
def index():
    '''Check whether DS has been updated.'''
    # if DS_M.shape[0] != len(Urls.query.all()):
    #    mk_matrix_from_db()
    results = []
    internal_message = ""
    query = request.args.get('q')
    print(request, request.args, query)
    num_entries = len(Urls.query.all())
    me = Pods.query.all()[0]
    if not query:
        return render_template("search/index.html", num_entries=num_entries, name=me.name, description=me.description)
    else:
        results = []
        query = query.lower()
        pears = ['0.0.0.0']
        results, pods = score_pages.run(query, pears)
        return render_template('search/results.html', pears=pears, query=query, results=results[:20], num_entries=num_entries, name=me.name, description=me.description)


@search.route('/html_cache/<path:filename>')
def custom_static(filename):
    return send_from_directory('html_cache', filename)
