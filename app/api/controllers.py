# Import flask dependencies
import numpy as np
from app.utils import normalise, convert_to_array, convert_to_string, convert_string_to_dict
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
    DS_vector = np.zeros(400)
    word_vector = ""
    freqs = {}
    for u in Urls.query.all():
        DS_vector+=convert_to_array(u.vector)
        for k,v in convert_string_to_dict(u.freqs).items():
            if k in freqs:
                freqs[k]+=int(v)
            else:
                freqs[k]=int(v)
    DS_vector = convert_to_string(normalise(DS_vector))
    c = 0
    for w in sorted(freqs, key=freqs.get, reverse=True):
        word_vector+=w+':'+str(freqs[w])+' '
        c+=1
        if c == 300:
            break
    self = Pods.query.all()[0]
    name = self.name
    description = self.description
    language = self.language
    return jsonify(DSvector=DS_vector, name=name, description=description, language=language, wordvector=word_vector)
    
