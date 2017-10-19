from sqlalchemy import select
from bd_informatica import cli_table, ven_table
from bd_informatica import engine
import os

# conn = engine.connect()

data = select([ven_table.c.VEN_ID, ven_table.c.VEN_NOME]).execute()
print(data)
print(list(data))

#lista = list()
#for row in select([ven_table]).execute():
#   lista.append(row)
#print(lista)