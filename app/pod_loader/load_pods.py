import requests, csv
from os.path import dirname, join, realpath
from app import db
from app.api.models import Pods, Urls
from app.utils import readPods, get_pod_info
from app.utils_db import pod_from_json, url_from_json, pod_from_file, pod_from_scratch
from app.pod_loader import score_pods, index_pod_file
from app.pod_loader.update_pod_list import update_pod_list

dir_path = dirname(dirname(dirname(realpath(__file__))))


def index_file():
    c = 0
    urls = list()
    pod_name = ""
    f = open(join(dir_path, "app", "static", "pods", "urls_from_pod.csv"), 'r', encoding="utf-8")
    for l in f:
        if "#Pod name" in l:
            pod_name = l.rstrip('\n').replace("#Pod name:", "")
        fields = l.rstrip('\n').split(',')
        if len(fields) == 7:
            url, title, snippet, vector, freqs, cc = index_pod_file.parse_line(fields)
            if not db.session.query(Urls).filter_by(url=url).all():
                u = Urls(
                    url=url,
                    title=title,
                    snippet=snippet,
                    pod=pod_name,
                    vector=vector,
                    freqs=freqs,
                    cc=cc)
                urls.append(u)
    f.close()
    if len(urls) == 0:
        print("All URLs already known.")
    else:
        for u in urls:
            db.session.add(u)
            db.session.commit()
            c += 1
            pod_from_file(pod_name)


'''Take a file of pod URLs and index all URLs on each pod.'''
def subscribe():
    print("Subscribing to public pods")
    pods=update_pod_list()
    for p in pods:
        pod_from_scratch(str(p[0]),str(p[1]),str(p[2]),str(p[3]))
    f = join(dir_path, "app", "static", "pods", "pods_to_index.txt")
    print("Reading", f)
    pod_urls = readPods(f)
    urls = []
    for pod_url in pod_urls:
        print(pod_url)
        pod_url = str(pod_url)
        pod_entry = db.session.query(Pods).filter_by(url=pod_url).first()
        pod_entry.registered = True
        db.session.commit()
        with requests.Session() as s:
            download = s.get(pod_url)
            decoded_content = download.content.decode('utf-8')
            crows = csv.reader(decoded_content.splitlines(), delimiter=',')
            records = list(crows)
        for u in records:
            if len(u) == 7:
                url, title, snippet, vector, freqs, cc = index_pod_file.parse_line(u)
                if not db.session.query(Urls).filter_by(url=url).all():
                    u = Urls(
                        url=url,
                        title=title,
                        snippet=snippet,
                        pod=pod_entry.name,
                        vector=vector,
                        freqs=freqs,
                        cc=cc)
                    urls.append(u)
    if len(urls) == 0:
        print("All URLs already known.")
    else:
        c = 0
        for u in urls:
            #print("Adding",u.url,"to DB")
            db.session.add(u)
            db.session.commit()
            c += 1


index_file()
#subscribe()
