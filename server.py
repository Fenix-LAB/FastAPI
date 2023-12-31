from fastapi import FastAPI
import uvicorn
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json

from schemas.models import Fruit, FruitList
from config.database import base, engine, session
from models.fruits import Fruit as FruitTable

base.metadata.create_all(bind=engine)

app = FastAPI()

# Test de endpoints para llenar una tabla

# table_fruits = []

# Endponit Post para añadir frutas
@app.post("/create_fruit", status_code=status.HTTP_201_CREATED, response_model=Fruit, summary="Crear nueva lista")
def add_fruit(Fruit: Fruit):
    """
    ## ARGS
        - id: optional
        - name: string
        - sugar: integrer

    """
    # try:
        # new_id = table_fruits[-1].id
        # print(new_id)
    # except:
    #     new_id = 0

    # print(new_id)
    # table_fruits.append({"id":new_id + 1, "name":Fruit.name, "sugar": Fruit.sugar})
    # print(table_fruits)
    # Fruit.id = new_id + 1
    # table_fruits.append(Fruit)
    # return {"id":new_id + 1, "name":Fruit.name, "sugar": Fruit.sugar}
    # print(table_fruits)

    db = session()
    new_fruit = FruitTable(**Fruit.model_dump())
    db.add(new_fruit)
    db.commit()
    return Fruit.model_dump()

# Endpoint Get para obtener la fruta de algun ID
@app.get("/all", status_code=status.HTTP_200_OK, response_model=FruitList, summary="Retorna todos los datos")
def get_all_fruits():  
    """
    ## RESPONSE
        - Return FruitList

    """
    # return json.loads(json.dumps(table_fruits))
    db = session()
    result = db.query(FruitTable).all()
    # return FruitList(ListF=table_fruits)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))

# Endpoint Get para obtener la fruta de algun ID
@app.get("/{id}", status_code=status.HTTP_200_OK)
def get_fruit(id_f: int):
    """
    ## RESPONSE
        - Return Fruit

    """
    # for fruit in table_fruits:
    #     if fruit.id == id_f:
    #         return fruit 
    db = session()
    result = db.query(FruitTable).filter(FruitTable.id == id_f).first()
    print(result)
    # return {}
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message":"Fruit not found"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))
# Endpoint Delete para eliminar una fruta de la lista
@app.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_fruit(id_f: int):
    """
    ## RESPONSE
        - Delete Fruit

    """
    # for fruit in table_fruits:
    #     if fruit.id == id_f:
    #         table_fruits.remove(fruit)
    #         return fruit 
    db = session()
    result = db.query(FruitTable).filter(FruitTable.id == id_f).first()
    # return {}
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message":"Fruit not found"})
    
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))


# Endpoint Patch para actualizar un campo de la tabla
@app.patch("/{id}", status_code=status.HTTP_200_OK, response_model=Fruit)
def update_fruit(id_f: int, Fruit: Fruit):
    # for fruit in table_fruits:
    #     if fruit.id == Fruit.id:
    #         fruit.name = Fruit.name
    #         return fruit
    db = session()
    result = db.query(FruitTable).filter(FruitTable.id == id_f).first()
    # return {}
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message":"Fruit not found"})
    if result:
        for attr, value in Fruit.model_dump().items():
            setattr(result, attr, value)
        db.commit()
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)