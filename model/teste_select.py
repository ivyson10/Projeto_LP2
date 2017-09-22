
from sqlalchemy import select
from tb_restaurante import tb_cliente, tb_produto


s = select([tb_produto])

for row in s.execute():
    print(row)