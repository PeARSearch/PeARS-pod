# Import flask and template operators
from flask import Flask

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Sample HTTP error handling
#@app.errorhandler(404)
#def not_found(error):
#    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.api.controllers import api as api_module
from app.search.controllers import search as search_module
from app.pages.controllers import pages as pages_module

# Register blueprint(s)
app.register_blueprint(api_module)
app.register_blueprint(search_module)
app.register_blueprint(pages_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
#db.drop_all()
db.create_all()

# Populate pod from CSV file. Can be commented out after first use.
from app.api import read_urls_csv

# Populate templates with pod info from self.txt
from app.api.models import Pods

self_info = open("me.txt",'r')
tmp = {}
for l in self_info:
    l = l.rstrip('\n')
    fields = l.split(" = ")
    tmp[fields[0]] = fields[1]
self_info.close()

print(tmp)
if len(Pods.query.all()) == 0 and 'name' in tmp and 'description' in tmp and 'language' in tmp:
    self = Pods(name=tmp['name'], description=tmp['description'], language=tmp['language'])
    db.session.add(self)
    db.session.commit()
