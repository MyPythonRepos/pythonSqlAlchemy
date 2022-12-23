from sqlalchemy import  create_engine, MetaData, Table,Column,Integer,String, Float, DateTime, ForeignKey
from datetime import datetime


def create_database():
  engine = create_engine("sqlite:///database/basedatos.db", echo=False)
  print("en bbdd")
  tablenames = engine.table_names()
  if not tablenames:
    metadata = MetaData(engine)
    connection = engine.connect()
    if not engine.dialect.has_table(connection, "users"):
      Table("users", metadata,
              Column('iUser_cod', Integer, primary_key=True), 
              Column('tName', String(20), unique=True), 
              Column('tPass', String(20), nullable=False),
              Column('dCreated', DateTime(), default=datetime.now),
              Column('dModified', DateTime(), default=datetime.now, onupdate=datetime.now),
              sqlite_autoincrement=True)
    
    if not engine.dialect.has_table(connection, "activities"):
      Table("activities", metadata,
              Column('iActivity_id', Integer, primary_key = True),
              Column('tName', String(30), nullable=True, unique=True),
              Column('tDescription', String(60)),
              Column('dCreated', DateTime(), default=datetime.now),
              Column('dModified', DateTime(), default=datetime.now, onupdate=datetime.now),
              sqlite_autoincrement=True)

    if not engine.dialect.has_table(connection, "trainings"):
      Table("trainings", metadata,  
              Column('iTraining_cod', Integer, primary_key = True),
              Column('iUser_cod', Integer, ForeignKey("users.iUser_cod", ondelete="CASCADE", onupdate="CASCADE"), nullable=False),
              Column('iActivity', Integer, ForeignKey("activities.iActivity_id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False),
              Column('iDistance', Float),
              Column('iDuration', String(10)),
              Column('dCreated', DateTime(), default=datetime.now),
              Column('dModified', DateTime(), default=datetime.now, onupdate=datetime.now),
              sqlite_autoincrement=True)

    # Implement the creation
    metadata.create_all()