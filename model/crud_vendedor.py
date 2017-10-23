from sqlalchemy import update, delete, select
from model.bd_informatica import ven_table, engine
import bcrypt


def insert_vendedor(cpf, rg, nome, telefone, email, senha):
    conn  = engine.connect()
    ins = ven_table.insert()
    new_vendedor = ins.values([None,cpf, rg, nome, telefone, email, bcrypt.hashpw(senha.encode('utf-8'),bcrypt.gensalt())])
    conn.execute(new_vendedor)


def update_vendedor(id):
    conn = engine.connect()
    upd = update(ven_table).where(ven_table.c.VEN_ID == id)
    cpf = input("cpf:")
    rg = input("rg:")
    nome = input("nome:")
    telefone = input("telefone:")
    email = input("email:")
    senha = input("senha:")
    upd = upd.values([id, cpf, rg, nome, telefone, email, bcrypt.hashpw(senha.encode('utf-8'),bcrypt.gensalt())])
    conn.execute(upd)


def delete_vendedor(id):
    conn = engine.connect()
    delet = delete(ven_table).where(ven_table.c.VEN_ID == id)
    conn.execute(delet)
    
def pesquisa_vendedor(cpf):
        data = select([ven_table.c.VEN_ID, ven_table.c.VEN_NOME]).where(ven_table.c.VEN_CPF == cpf).execute()
        lista = list(data)
        for row in lista:
            pass
        return row
def pesquisa_vendedor_all():
        data = select([ven_table.c.VEN_ID, ven_table.c.VEN_NOME]).execute()
        lista = list(data)
        return lista

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