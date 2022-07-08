import json
from unittest import mock
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

    

# get api/products_category/<category>
# return all the products whose category is 

@app.get("/api/products_category/<category>")
def get_prod_by_category(category):
    print("your category", category)
    results=[]
    for prod in mock_data:
        if prod["category"].lower()==category.lower():
            results.append(prod)
       
    return json.dumps(results)
   


# search for cheapest product by price with end page


@app.get("/api/product_cheapest")
def get_cheap_prices():

    solution=mock_data[0]
    for prod in mock_data:
        if prod["price"] < solution["price"]:
            solution=prod 

    return json.dumps(solution)

## get /api/categories
    ## - return ok
    ##- travel mock data and print category of every product
    # -  put the category in a list and at the end of for loop, return the list as json
@app.get("/api/categories")
def get_category():
    
    prods=[]
    for category in mock_data:
        cat = category["category"]
        if not cat in prods:
            prods.append(cat)
    
    return json.dumps(prods)
    # print (category["category"])

    # return "OK"  




app.run(debug=True)

