from bson import ObjectId
from flask import Flask, request
from about import me
from data import mock_data
import random
import json
from config import db
from flask_cors import CORS

app = Flask("server")
CORS(app) # allow requests from any origin

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

def fix_mongo_id(obj):
    obj["id"]=str(obj["_id"])
    del obj["_id"]
    return obj

# #######################################################################################################################################


# get /api/products
# return mock_data as a json string
@app.get("/api/products")
def data_json():

    cursor= db.products.find({})
    results=[]
    for prod in cursor:
        fix_mongo_id(prod)
        results.append(prod)

    return json.dumps(results) 


# @app.post("/api/products")
# def save_product():
#     data=request.get_json()
#     print(data)

#     return "POST OK"

@app.post("/api/products") 
def save_product(): 
    product=request.get_json()

    # save the product
    db.products.insert_one(product)
    
    # fix the id
    product["id"]= str (product["_id"])

    del product["_id"]

    return json.dumps(product)
# ################
@app.get("/api/products/<id>")
def get_product_by_id(id):
    prod= db.products.find_one({"_id": ObjectId(id)})
    if not prod:
        return "NOT FOUND"

    fix_mongo_id(prod)
    return json.dumps(prod)

    
        
    

    

# get api/products_category/<category>
# return all the products whose category is 

@app.get("/api/products_category/<category>")
def get_prod_by_category(category):
    cursor= db.products.find({"category":category})
    results =[]
    for prod in cursor:
        fix_mongo_id(prod)
        results.append(prod)
    
    
    return json.dumps(results)
   


# search for cheapest product by price with end page


@app.get("/api/product_cheapest")
def get_cheap_prices():

    cursor= db.products.find({})
    solution=cursor[0]
    for prod in cursor:
        if prod["price"] < solution["price"]:
            solution=prod 

    fix_mongo_id(solution)
    return json.dumps(solution)

## get /api/categories
    ## - return ok
    ##- travel mock data and print category of every product
    # -  put the category in a list and at the end of for loop, return the list as json
@app.get("/api/categories")
def get_category():

    cursor= db.products.find({})
    prods=[]
    for category in cursor:
        cat = category["category"]
        if not cat in prods:
            prods.append(cat)

    
    return json.dumps(prods)
    # print (category["category"])

    # return "OK"  
@app.get("/api/count_products")
def get_prod_count():

    cursor=db.products.find({})
    count=0
    for prod in cursor:
        count+= 1
    
    
    
    return json.dumps({"count":count})


@app.get("/api/search/<text>")
def search_products(text):
    results=[]
    text = text.lower()
    for product in mock_data:
        if text in product["title"].lower():
            results.append(product)

    return json.dumps(results)


################################################################
################## API  Endpoints= Coupons ####################
################################################################


# @app.get("/api/coupons")
# def search_coupons():



app.run(debug=True)

