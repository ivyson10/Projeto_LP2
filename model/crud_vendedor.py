from sqlalchemy import update, delete
from model.bd_informatica import ven_table, engine
import bcrypt


def insert_vendedor(cpf, rg, nome, telefone, email, senha):
    conn  = engine.connect()
    ins = ven_table.insert()
    new_vendedor = ins.values([ cpf, rg, nome, telefone, email, senha])
    conn.execute(new_vendedor)

def update_vendedor(id,cpf, rg, nome, telefone, email,senha):
    conn = engine.connect()
    upd = update(ven_table).where(ven_table.c.id == id)
    upd = upd.values(cpf, rg, nome, telefone, email,senha)
    conn.execute(upd)


def delete_vendedor(id):
    conn = engine.connect()
    delet = delete(ven_table).where(ven_table.c.id == id)
    conn.execute(delet)