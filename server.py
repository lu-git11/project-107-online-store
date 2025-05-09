
# to create a virtual enviormnet 
# py -m virtual enviromen  (name of enviroment)
# # py -m venv venv
# activate venv - venv\Scripts\activate
# install flask - py -m install flask pymongo "pymongo[srv]" certif
# pip freeze to see package installed
# py server.py to run script

from flask import Flask, render_template, request
import json
from config import db
from flask_cors import CORS


app = Flask(__name__)
CORS(app) # this disables CORS policy (protects server from outsiders)

@app.route("/")   #get URL
def hello_world():   #function
    return "<p>Hello, World!</p>"   #return

@app.get("/test")
def test():
    return "This is a test."

@app.get("/home")
def home():
    return "welcome to home page"

@app.get("/users")
def get_users():
    return{"users": ["alice", "bob", "charlie"]}

@app.get("/api/about")
def about():
    name = {"name": "jeff"}
    return name

@app.get("/api/students")
def students():
    student_name = ["jeff", "isai", "george"]
    return student_name

@app.get("/greet/<name>")
def greet(name):
    print("Greet endpoint access")
    # return "Hello " + name
    return f"hello {name}"

@app.get("/contact") 
def contact_api():
    print("contact api andpoint acess")
    name = "michael"
    age = 20
    return render_template("contact.html", name=name, age=age)


@app.get("/api/products")
def get_products():
    products = []
    cursor = db.products.find({})
    for prod in cursor:
        products.append(fix_id(prod))

    return json.dumps(products)

def fix_id(obj):
    obj['_id'] = str(obj["_id"])
    return obj

@app.post("/api/products")
def post_products():
    item = request.get_json()
    print(item)   
    db.products.insert_one(item)
    print(item)
    #mock save
    # products.append(item)
    return json.dumps(fix_id(item)) 

@app.get("/api/categories")
def get_categories():
    categories = []
    cursor = db.products.find({})
    for prod in cursor:
        prod["category"]
        cat = prod["category"]
        if cat not in categories:
            categories.append(cat)

    return json.dumps(categories)
    

@app.put("/api/products/<int:index>")
def put_products(index):
    update_item = request.get_json()
    if len(products)> index >= 0:
        products[index]= update_item
        return json.dumps(update_item)
    else:
        return "that index does not exist" 
    
@app.delete("/api/products/<int:index>")
def delete_products(index):
    delete_item = request.get_json()
    if len(products)> index >= 0:
        delete_item = products.pop(index)
        return json.dumps(delete_item)
    else:
        return "that index does not exist"
    
@app.patch("/api/products/<int:index>")
def patch_products(index):
    patch_item = request.get_json()
    if len(products)> index >= 0:
        products(index).update(patch_item)
        return json.dumps(patch_item)
    else:
        return "that index does not exist"
    

@app.get("/api/reports/total")
def total():
    total = 0
    cursor = db.products.find({})
    for prod in cursor:
        prod["price"]
        total += prod["price"]
    
    return json.dumps(total)


@app.post("/api/coupons")
def post_coupons():
    coupon = request.get_json()  
    db.coupons.insert_one(coupon)
    
    return json.dumps(fix_id(coupon)) 

@app.get("/api/coupons")
def get_coupons():
    results = []
    cursor = db.coupons.find({})
    for coupon in cursor:
        results.append(fix_id(coupon))

    return json.dumps(results)



app.run(debug=True, port=8000)


        