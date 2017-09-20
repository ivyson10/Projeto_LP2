from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, Float

database  = "mysql+mysqldb://root:xrl832k.@localhost:3306/bdvendas.db"

engine = create_engine(database,echo = True)
if not database_exists(engine.url):
    create_database(engine.url)

metadata = MetaData(bind=engine)

