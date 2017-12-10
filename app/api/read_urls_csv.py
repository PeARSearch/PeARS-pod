from app.api.models import Urls
from app import db
import os
import logging

dir_path = os.path.dirname(os.path.realpath(__file__))

def parse_line(l):
    fields = l.rstrip('\n').split(',')
    url = fields[1]
    title = fields[2]
    snippet = fields[3]
    vector = fields[4]
    freqs = fields[5]
    cc = False
    if fields[6] == "True":
        cc = True
    return url, title, snippet, vector, freqs, cc

if os.path.isfile(os.path.join(dir_path, "urls_db.csv")):
    f = open(os.path.join(dir_path, "urls_db.csv"),'r')
    for l in f:
        url, title, snippet, vector, freqs, cc = parse_line(l)
        if not db.session.query(Urls).filter_by(url=url).all():
            u = Urls(url=url, title=title, snippet=snippet, vector=vector, freqs=freqs, cc=cc)
            db.session.add(u)
            db.session.commit()
f.close()
