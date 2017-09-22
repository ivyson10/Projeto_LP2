from model.bd_informatica import cli_table, engine
from sqlalchemy import updaye, select, delete

def insert_cliente(cpf, rg, nome, telefone, email, dt_nasc):
    conn  = engine.connect()
    ins = cli_table.insert()
    new_cliente = ins.values(["",cpf, rg, nome, telefone, email, dt_nasc])
    conn.execute(new_cliente)