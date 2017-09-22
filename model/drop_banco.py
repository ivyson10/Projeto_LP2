from sqlalchemy import create_engine
from sqlalchemy_utils import drop_database

database = 'mysql+mysqldb://root:xrl832k.@localhost:3306/restaurante.db'
    
engine = create_engine(database, echo=True)
drop_database(engine.url)