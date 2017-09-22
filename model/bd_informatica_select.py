from sqlalchemy import select
import bd_informatica

s = select([cli_table, ven_table,
            for_table, prod_table])

# for row in s.execute():
#    print(row)