# Repositorio test de FastAPI

## Para instalar el modulo de FastAPI se usa el siguiente comando:

```bash
pip install fastapi
```

## Se debe instalar el servidor de Uvicorn, que es el que nos permite montar el backend

```bash
pip install "uvicorn[standard]"
```

## Primero usa el siguiente codigo para lanzar el servidor:

```python
from typing import Union
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

## Para lanzar el servicio de forma local se usa el siguinte comando:

```bash
uvicorn server:app --reload
```