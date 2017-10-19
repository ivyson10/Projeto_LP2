from sqlalchemy import update, delete, select
from model.bd_informatica import ven_table, engine
import bcrypt


def insert_vendedor(cpf, rg, nome, telefone, email, senha):
    conn  = engine.connect()
    ins = ven_table.insert()
    new_vendedor = ins.values([None,cpf, rg, nome, telefone, email, bcrypt.hashpw(senha.encode('utf-8'),bcrypt.gensalt())])
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

def valida_senha(usuario, senha):
    s = select([ven_table])
    for row in s.execute():
        if(row[3] == usuario):
            salt = row[-1].encode('utf-8')
            senha_hashed = bcrypt.hashpw(senha.encode("utf-8"), salt)
            return str(senha_hashed) == str(salt)
    return False

if __name__ == '__main__':
    print(valida_senha(input("User: "), input('Senha: ')))