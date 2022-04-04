from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)

items = [
    {"name": "asdfjasd", "price": 324},
    {"name": "asdsdsdad", "price": 3224},
    {"name": "asASddsaasd", "price": 3124},
    {"name": "4234232432asASddsaasd", "price": 3124},
]

cart = []

@app.get("/")
def index():
    return render_template("index.html", items=items, cart=cart)

@app.get("/<int:id>")
def get_item(id):
    if id > len(items):
        abort(404)
    return render_template("item.html", item=items[id], id=id)

@app.get("/cart/add")
def cart_add():
    if 'id' in request.args:
        id = int(request.args["id"])
        cart.append(items[id])
    return redirect(url_for('index'))  

@app.get("/cart/remove")
def cart_remove():
    if 'id' in request.args:
        id = int(request.args["id"])
        del cart[id]
    return redirect(url_for('index'))