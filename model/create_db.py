from sqlalchemy import create_engine
from sqlalchemy_utils import drop_database, create_database
from bd_informatica import metadata

database = 'mysql+mysqldb://root:xrl832k.@localhost:3306/bdvendas.db'
    
engine = create_engine(database, echo=True)
drop_database(engine.url)
create_database(engine.url)

metadata.drop_all()
metadata.create_all()

print('done.')