# Import flask dependencies
import numpy as np
from app.utils import normalise, convert_to_array, convert_to_string
from flask import Blueprint, jsonify
from app.api.models import dm_dict_en, Pods, Urls

# Define the blueprint:
api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/vectors/<word>/')
def return_vector(word):
    v = list(dm_dict_en[word])
    return jsonify(vector=v)

@api.route('/pods/')
def return_pods():
    return jsonify(json_list = [p.serialize for p in Pods.query.all()])

@api.route('/urls/')
def return_urls():
    return jsonify(json_list=[i.serialize for i in Urls.query.all()])

@api.route('/self/')
def return_self():
    vector = np.zeros(400)
    for u in Urls.query.all():
        vector+=convert_to_array(u.vector)
    vector = convert_to_string(normalise(vector))
    test = "test"
    return jsonify(vector=vector, description=test)
    
