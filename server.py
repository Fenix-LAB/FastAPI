# from typing import Union
from fastapi import FastAPI
import uvicorn
from fastapi import status
import json

app = FastAPI()

# Test de endpoints para llenar una tabla

table_fruits = [{"id": 1, "name": "Apple"}]

# Endponit Post para añadir frutas
@app.post("/create_fruit", status_code=status.HTTP_201_CREATED)
def add_fruit(name: str):
    new_id = table_fruits[-1]["id"]
    # print(new_id)
    table_fruits.append({"id":new_id + 1, "name":name})
    # print(table_fruits)
    return {"id": new_id + 1, "name": name}

# Endpoint Get para obtener la fruta de algun ID
@app.get("/all", status_code=status.HTTP_200_OK)
def get_all_fruits():  
    return json.loads(json.dumps(table_fruits))

# Endpoint Get para obtener la fruta de algun ID
@app.get("/{id}", status_code=status.HTTP_200_OK)
def get_fruit(id_f: int):
    for fruit in table_fruits:
        if fruit["id"] == id_f:
            return fruit 

    return {}

# Endpoint Delete para eliminar una fruta de la lista
@app.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_fruit(id_f: int):
    for fruit in table_fruits:
        if fruit["id"] == id_f:
            table_fruits.remove(fruit)
            return fruit 

    return {}

# Endpoint Patch para actualizar un campo de la tabla
@app.patch("/{id}", status_code=status.HTTP_200_OK)
def update_fruit(id_f: int, name: str):
    for fruit in table_fruits:
        if fruit["id"] == id_f:
            fruit["name"] = name
            return fruit

    return {}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)