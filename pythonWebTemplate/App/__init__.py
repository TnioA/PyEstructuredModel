from flask import Flask, render_template, jsonify

# Import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy ###################

app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
#db = SQLAlchemy(app) ###################

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({ 'Result': 'Not found' }), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from App.Controller.AddressController import addressController

# Register blueprint(s)
app.register_blueprint(addressController)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
#db.create_all() ###################