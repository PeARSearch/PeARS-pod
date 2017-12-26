from app.api.models import Urls
from app import db
import os
import logging

def parse_line(l):
    fields = l.rstrip('\n').split(',')
    url = fields[1]
    title = fields[2]
    snippet = fields[3]
    vector = fields[4]
    freqs = fields[5]
    cc = fields[6]
    if cc == "True":
        cc = True
    return url, title, snippet, vector, freqs, cc

if os.path.isfile("urls_db.csv"):
    f = open("urls_db.csv",'r')
    for l in f:
        url, title, snippet, vector, freqs, cc = parse_line(l)
        if not db.session.query(Urls).filter_by(url=url).all():
            print(url)
            u = Urls(url=url, title=title, snippet=snippet, vector=vector, freqs=freqs, cc=cc)
            db.session.add(u)
            db.session.commit()
f.close()
