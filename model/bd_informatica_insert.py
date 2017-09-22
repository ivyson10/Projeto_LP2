import bd_informatica 

conn = engine.connect()

ins_cli = cli_table.insert()
ins_ven = ven_table.insert()
ins_for = for_table.insert()
ins_prod = prod_table.insert()

#new_cli = ins.values(nome='Fabio', etc)

#conn.execute(new_cli)