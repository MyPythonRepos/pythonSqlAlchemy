# INFO:
# 
# https://overiq.com/sqlalchemy-101/defining-schema-in-sqlalchemy-core/

import db
import os
from datetime import datetime

DATABASE = './database/basedatos.db'

def check_database():
  print(os.path.getsize(DATABASE))
  if not os.path.exists(os.path.dirname(DATABASE)):
    os.mkdir('./database')
    print(str(datetime.now()) + " Creado el directorio de base de datos")
  if os.path.getsize(DATABASE) >= 28672:    
    db.create_database()
    print(str(datetime.now()) + " Creada la base de datos")

if __name__ == "__main__":
  check_database()