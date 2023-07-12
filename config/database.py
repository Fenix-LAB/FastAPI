import os

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import declarative_base

sqlite_file = '../database/database.sql'
base_dir = os.path.dirname(os.path.realpath(__file__))
print("Aqui")
print("dir:", os.path.join(base_dir, sqlite_file))
abs_path = 'sqlite:///D:\Documentos\Python\BACKEND\FastAPI\database.sql'
# database_url = f'sqlite:///{os.path.join(base_dir, sqlite_file)}'

engine = create_engine(abs_path, echo=True)

session = sessionmaker(bind=engine)

base = declarative_base()