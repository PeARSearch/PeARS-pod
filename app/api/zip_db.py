from app.submit_urls.models import Urls


def read_db():
    for u in Urls.query.all():
        print(u.url)

read_db()
