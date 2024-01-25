from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "Baby's First Store",
        "items": [
            {
                "name": "steel chair",
                "price": 19.98
            }
        ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores": stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:this_store>/item")
def create_item(this_store):
    request_data = request.get_json()
    new_item = {"name": request_data["name"], "price": request_data["price"]}
    for store in stores:
        if store["name"] == this_store:
            store["items"].append(new_item)
            return new_item, 201
    return {"message": f"Store {this_store} not found"}, 404

@app.get("/store/<string:this_store>")
def get_store(this_store):
    for store in stores:
        if store["name"] == this_store:
            return store
    return {"message": f"Store {this_store} not found"}, 404

@app.get("/store/<string:this_store>/item")
def get_items(this_store):
    for store in stores:
        if store["name"] == this_store:
            return {"items": store["items"]}
    return {"message": f"Store {this_store} not found"}, 404

@app.get("/store/<string:this_store>/item/<string:this_item>")
def get_item(this_store, this_item):
    for store in stores:
        if store["name"] == this_store:
            for item in store["items"]:
                if item["name"] == this_item:
                    return item
            return {"message": f"Item {this_item} not found in store {this_store}"}, 404
    return {"message": f"Store {this_store} not found"}, 404