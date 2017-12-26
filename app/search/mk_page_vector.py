import re
import numpy as np
import logging
import string
from app import db
from app.api.models import dm_dict_en, Urls
from app.utils import convert_to_string, convert_dict_to_string, normalise

num_dimensions = 400

stopwords = ["", "(", ")", "a", "about", "an", "and", "are", "around", "as", "at", "away", "be", "become", "became",
             "been", "being", "by", "did", "do", "does", "during", "each", "for", "from", "get", "have", "has", "had",
             "he", "her", "his", "how", "i", "if", "in", "is", "it", "its", "made", "make", "many", "most", "not", "of",
             "on", "or", "s", "she", "some", "that", "the", "their", "there", "this", "these", "those", "to", "under",
             "was", "were", "what", "when", "where", "which", "who", "will", "with", "you", "your"]

def clean_text(text):
    text = re.findall(r"[\w']+|[.,!?;':]", text.lower())
    return text

def compute_freq_vector(text):
    freqs = {}
    for w in text:
        if w not in stopwords and w not in string.punctuation:
            if w in freqs:
                freqs[w]+=1
            else:
                freqs[w]=1
    return freqs


def compute_query_vectors(query):
    """ Make distribution for query """
    words = query.rstrip('\n').split()
    # Only retain arguments which are in the distributional semantic space
    vecs_to_add = []
    words_for_freqs = []
    for word in words:
        words_for_freqs.append(word)
        if word in dm_dict_en:
          vecs_to_add.append(word)

    vbase = np.array([])
    # Add vectors together
    if vecs_to_add:
        # Take first word in vecs_to_add to start addition
        vbase = dm_dict_en[vecs_to_add[0]]
        for vec in vecs_to_add[1:]:
            vbase = vbase + dm_dict_en[vec]

    vbase = normalise(vbase)
    freqs = compute_freq_vector(words_for_freqs)
    return vbase, freqs
