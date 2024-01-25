from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "Baby's First Store",
        "items": [
            {
                "name": "steel chair",
                "price": 1998.00
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
    return {"message":"Store not found"}, 404