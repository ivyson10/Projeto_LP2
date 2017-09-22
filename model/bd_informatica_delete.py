from sqlalchemy import delete
import bd_informatica

#from bd_informatica import cli_table, engine

conn = engine.connect()

# d = delete(cli_table).where(cli_table.c.CLI_NOME == 'Joao')

# result = conn.execute(d)

# print(result.rowcount)