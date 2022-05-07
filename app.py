# config
from flask import Flask
app = Flask(__name__)

# index route
@app.route("/")
def index():
    return("Hello, this is PetFax")

# pets route
@app.route("/pets")
def pets():
    return("These are our pets available for adoption!")

@app.route("/pets/<pet>")
def show_pets(pet):
    return(f"This pet is a(n) {pet} and here are some fun facts about it!")

@app.route("/facts")
def facts():
    return("This is the fact page! here are some facts about the pets!")
    
