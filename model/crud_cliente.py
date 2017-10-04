from model.bd_informatica import cli_table, engine
#from sqlalchemy import updade, select, delete

def insert_cliente(cpf, rg, nome, telefone, email):
    conn  = engine.connect()
    ins = cli_table.insert()
    new_cliente = ins.values([cpf, rg, nome, telefone, email])
    conn.execute(new_cliente)