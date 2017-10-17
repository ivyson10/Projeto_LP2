from sqlalchemy import (create_engine, MetaData, Column, Table, Integer, String, Date, DateTime,Numeric, ForeignKey)
from sqlalchemy_utils import create_database, database_exists

database  = "mysql+mysqldb://root:xrl832k.@localhost:3306/bdvendas.db"
engine = create_engine(database,echo = True)

metadata = MetaData(bind=engine)

cli_table = Table('tbCliente', metadata,
                    Column('CLI_ID', Integer, primary_key=True, nullable=False),
                    Column('CLI_CPF', String(15), nullable=False),
                    Column('CLI_RG', String(15), nullable=False),
                    Column('CLI_NOME', String(50), index=True),
                    Column('CLI_TEL', String(15), nullable=False),
                    Column('CLI_EMAIL', String(45)))

ven_table = Table('tbVendedor', metadata,
                    Column('VEN_ID', Integer, primary_key=True),
                    Column('VEN_CPF', String(15), nullable=False),
                    Column('VEN_RG', String(15), nullable=False),
                    Column('VEN_NOME', String(50), index=True),
                    Column('VEN_TEL', String(15), nullable=False),
                    Column('VEN_EMAIL', String(45)),
                    Column('VEN_SENHA', String(80), nullable =False))
                  
                   # Column('VEN_DT_NASC', Date),
                   # Column('VEN_DT_NASC', Numeric))

for_table = Table('tbFornecedor', metadata,
                    Column('FOR_ID', Integer, primary_key=True),
                    Column('FOR_CPF_CNPJ', String(15), nullable=False),
                    Column('FOR_NOME', String(50), index=True),
                    Column('FOR_TEL', String(15), nullable=False),
                    Column('FOR_EMAIL', String(45)),
                    Column('FOR_RUA', String(45)),
                    Column('FOR_BAIRRO', String(45)),
                    Column('FOR_CIDADE', String(45)),
                    Column('FOR_NUMERO', Integer))

prod_table = Table('tbProduto', metadata,
                    Column('PROD_ID', Integer, primary_key=True),
                    Column('PROD_QTDE', Integer),
                    Column('PROD_DESCR', String(50), index=True),
                    Column('PROD_PRECO', Numeric))

venda_table = Table('tbVenda', metadata,
                    Column('VENDA_ID', Integer, primary_key=True),
                    Column('VEN_ID', Integer, ForeignKey('tbVendedor.VEN_ID')),
                    Column('CLI_ID', Integer, ForeignKey('tbCliente.CLI_ID')),
                    Column('VENDA_DT', Date),
                    Column('VENDA_FRETE', Numeric),
                    Column('VENDA_HORARIO', DateTime),
                    Column('FOR_RUA', String(45)),
                    Column('FOR_BAIRRO', String(45)),
                    Column('FOR_CIDADE', String(45)),
                    Column('FOR_NUMERO', Integer),
                    Column('VENDA_TIPO_PAG', String(45)))

emite_table = Table('tbEmite', metadata,
                    Column('EMITE_ID', Integer, primary_key=True),
                    Column('PROD_ID', Integer, ForeignKey('tbProduto.PROD_ID')),
                    Column('CLI_ID', Integer, ForeignKey('tbCliente.CLI_ID')),
                    Column('EMITE_NUM_FISCAL', Integer))

fornece_table = Table('tbFornece', metadata,
                    Column('FORNECE_ID', Integer, primary_key=True),
                    Column('PROD_ID', Integer, ForeignKey('tbProduto.PROD_ID')),
                    Column('FOR_ID', Integer, ForeignKey('tbFornecedor.FOR_ID')),
                    Column('FORNECE_QTDE_PROD', Integer))

