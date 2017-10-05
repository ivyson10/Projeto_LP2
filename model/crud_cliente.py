from sqlalchemy import update, delete
from model.bd_informatica import cli_table, engine


def insert_cliente(cpf, rg, nome, telefone, email):
    conn  = engine.connect()
    ins = cli_table.insert()
    new_cliente = ins.values([cpf, rg, nome, telefone, email])
    conn.execute(new_cliente)

def update_cliente(id,cpf, rg, nome, telefone, email):
    conn = engine.connect()
    upd = update(cli_table).where(cli_table.c.id == id)
    upd = upd.values(cpf, rg, nome, telefone, email)
    conn.execute(upd)


def delete_cliente(id):
    conn = engine.connect()
    delet = delete(cli_table).where(cli_table.c.id == id)
    conn.execute(delet)