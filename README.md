# Repositorio test de FastAPI

#### Para instalar el modulo de FastAPI se usa el siguiente comando:

```bash
pip install fastapi
```

#### Se debe instalar el servidor de Uvicorn, que es el que nos permite montar el backend

```bash
pip install "uvicorn[standard]"
```

#### Primero usa el siguiente codigo para lanzar el servidor:

```python
from typing import Union
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

#### Para lanzar el servicio de forma local se usa el siguinte comando:

```bash
uvicorn server:app --reload
```
#### Para poder correr el servidor con el comando python, se agrega el siguinte codigo:

```python
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
```

#### Documentacion de los endpoints en: 
http://127.0.0.1:8000/docs

## Status code
- 200: OK
- 201: Created