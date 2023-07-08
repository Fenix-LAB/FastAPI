# from typing import Union
from fastapi import FastAPI
import uvicorn
from fastapi import status

app = FastAPI()

# Test de endpoints para llenar una tabla

table_fruits = [{"id": 1, "name": "Apple"}]


@app.post("/create_fruit", status_code=status.HTTP_201_CREATED)
def read_root(name: str):
    new_id = table_fruits[-1]["id"]
    # print(new_id)
    table_fruits.append({"id":new_id + 1, "name":name})
    # print(table_fruits)
    return {"id": new_id + 1, "name": name}

@app.get("/{id}", status_code=status.HTTP_200_OK)
def read_root(id_f: int):
    for fruit in table_fruits:
        if fruit["id"] == id_f:
            return fruit 

    return {}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)