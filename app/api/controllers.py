# Import flask dependencies
from flask import Blueprint, jsonify
from app.api.models import dm_dict_en, Pods, Urls

# Define the blueprint:
api = Blueprint('api', __name__, url_prefix='/pod0/api')

@api.route('/vectors/<word>/')
def return_vector(word):
    v = list(dm_dict_en[word])
    return jsonify(vector=v)

@api.route('/pods/')
def return_pods():
    return jsonify(json_list = Pods.query.all())

@api.route('/urls/')
def return_urls():
    return jsonify(json_list=[i.serialize for i in Urls.query.all()])
