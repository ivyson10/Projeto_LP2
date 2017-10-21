from sqlalchemy import select
from bd_informatica import cli_table, ven_table
from bd_informatica import engine
from crud_vendedor import insert_vendedor
import os


# conn = engine.connect()

data = select([ven_table.c.VEN_ID, ven_table.c.VEN_NOME]).where(ven_table.c.VEN_CPF == "1").execute()
lista = list(data)
print(lista)
for row in lista:
    print(row[1])
#lista = list()
#for row in select([ven_table]).execute():
#   lista.append(row)
#print(lista)