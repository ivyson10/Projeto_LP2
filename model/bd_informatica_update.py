from sqlalchemy import update
import bd_informatica

conn = engine.connect()

# u = update(cli_table).where(cli_table.c.CLI_NOME == 'Joao')

# u = u.values(CLI_NOME='novo nome')

# result = conn.execute(u)

# print(result.rowcount)
# rowcount conta quantas linhas foram alteradas