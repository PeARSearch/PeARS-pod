# Import flask and template operators
from flask import Flask

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from os.path import dirname,join,realpath

# Define the WSGI application object
app = Flask(__name__)

# Configurations
# app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
#@app.errorhandler(404)
#def not_found(error):
#    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.api.controllers import api as api_module
from app.pages.controllers import pages as pages_module
from app.search.controllers import search as search_module

# Register blueprint(s)
app.register_blueprint(api_module)
app.register_blueprint(pages_module)
app.register_blueprint(search_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.drop_all()
db.create_all()


# Populate templates with pod info from self.txt
from app.api.models import Pods

dir_path = dirname(dirname(realpath(__file__)))
self_info_file = open(join(dir_path, "me.txt"),'r')
self_info = {}
for l in self_info_file:
    l = l.rstrip('\n')
    fields = l.split(" = ")
    self_info[fields[0]] = fields[1]
self_info_file.close()

if len(Pods.query.all()) == 0 and 'name' in self_info and 'description' in self_info and 'language' in self_info:
    self = Pods(name=self_info['name'], description=self_info['description'], language=self_info['language'])
    db.session.add(self)
    db.session.commit()

# Populate pod from CSV file. Can be commented out after first use.
from app.pod_loader import load_pods
