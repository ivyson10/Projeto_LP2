from sqlalchemy import update, delete
from bd_informatica import for_table

def insert_fornecedor(cpf_cnpj, nome, telefone, email, rua, bairro, cidade, numero):
    conn  = engine.connect()
    ins = for_table.insert()
    new_fornecedor = ins.values([cpf_cnpj, nome, telefone, email, rua, bairro, cidade, numero])
    conn.execute(new_fornecedor)

def update_fornecedor(id,cpf_cnpj, nome, telefone, email, rua, bairro, cidade, numero):
    conn = engine.connect()
    upd = update(for_table).where(for_table.c.id == id)
    upd = upd.values(cpf_cnpj, nome, telefone, email, rua, bairro, cidade, numero)
    conn.execute(upd)


def delete_fornecedor(id):
    conn = engine.connect()
    delet = delete(for_table).where(ven_table.c.id == id)
    conn.execute(delet)