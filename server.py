
# to create a virtual enviormnet 
# py -m virtual enviromen  (name of enviroment)
# # py -m venv venv
# activate venv - venv\Scripts\activate
# pip freeze to see package installed

from flask import Flask, render_template, request
import json


app = Flask(__name__)


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
    # return f"hello {name}"

@app.get("/contact") 
def contact_api():
    print("contact api andpoint acess")
    name = "michael"
    return render_template("contact.html", name=name)

products = []
@app.get("/api/products")
def get_products():
    return json.dumps(products)

@app.post("/api/products")
def post_products():
    item = request.get_json()
    print(item)
    #mock save
    products.append(item)
    return json.dumps(item)

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

app.run(debug=True, port=8000)


