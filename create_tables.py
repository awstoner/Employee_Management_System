from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///employees.db', echo = True)
meta = MetaData()

employees = Table(
   'employees', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('age', Integer),
   Column('salary', Integer),
   Column('department_id', Integer),
   Column('address_id', Integer)
)
meta.create_all(engine)

engine = create_engine('sqlite:///address.db', echo = True)
meta = MetaData()

employees = Table(
   'address', meta, 
   Column('id', Integer, primary_key = True), 
   Column('street', String), 
   Column('city', String),
   Column('state', String)
)
meta.create_all(engine)

engine = create_engine('sqlite:///department.db', echo = True)
meta = MetaData()

employees = Table(
   'department', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('manager_id', Integer),
   Column('headquarters_address_id', Integer)
)
meta.create_all(engine)