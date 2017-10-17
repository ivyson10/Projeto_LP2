from sqlalchemy import select
from bd_informatica import cli_table, ven_table
import os

s = select([cli_table])

for row in s.execute():
    print(row)