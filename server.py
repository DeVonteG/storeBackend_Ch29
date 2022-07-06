import json
from flask import Flask
from about import me
from data import mock_data

app = Flask("server")

@app.get("/")
def home():
    return "Hello from flask server"

@app.get("/test")
def test():
    return "This is just a test"

@app.get("/about")
def about_me():
    return "About me, My Name is DeVonte"


################################################################
################## API  Endpoints= Products ####################
################################################################

@app.get("/api/version")
def version():
    return "Running ver 1.0"



@app.get("/api/about")
def about_json():
    return json.dumps(me) #parse the dictionary into a string

    # return me["first"] + " " + me["last"]

# get /api/products
# return mock_data as a json string
@app.get("/api/products")
def data_json():
    return json.dumps(mock_data) 


@app.get("/api/products/<id>")
def get_product_by_id(id):

    for prod in mock_data:
        if str(prod["id"]) == id:
            return json.dumps(prod)
        
    return "NOT FOUND"

app.run(debug=True)

