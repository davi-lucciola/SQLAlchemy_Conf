import sqlalchemy as sa
from sqlalchemy.future import Engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Optional
from conf.config_archive import config_archive
from dotenv import load_dotenv
from os import getenv


# DBMS INFOS
DB_CONFIG_PATH: str = './conf/__env'
DBMS: str = 'mysql'

# Engine
__engine: Optional[Engine] = None


# Functions
def create_engine(dbms: str) -> None:
    '''
    Create the global variable "__engine" to use in sqlalchemy
    '''
    global __engine
    if __engine: return

    conx_str: str = connection_str(dbms)
    # Creating Engine
    __engine = sa.create_engine(url=conx_str)
    create_tables()

def connection_str(dbms: str) -> str:
    '''
    Create the connection string with the dbms
    '''
    # Getting the amb variables
    user = getenv('USER_DB')
    password = getenv('PASSWD')
    host = getenv('HOST')
    port = getenv('PORT')
    database = getenv('DB')

    if dbms == 'mysql':
        user += ':' if password != '' else ''
        host += ':' if port != '' else ''
        conn_str = f'{dbms}+mysqlconnector://{user}{password}@{host}{port}/{database}'
    elif dbms == 'sqlite':
        conn_str = f'{dbms}:///{database}'
    
    return conn_str

def create_session(expire_on_commit = False) -> Session:
    '''
    Return a SQL Alchemy session to make a CRUD (Create, Read, Update and Delete)
    '''
    global __engine
    if not __engine: create_engine(DBMS)

    SessionDB = sessionmaker(bind=__engine, expire_on_commit=expire_on_commit)
    session: Session = SessionDB()

    return session

def create_tables() -> None:
    global __engine
    from models.model_base import Base
    if __engine is not None:
        if not sa.inspect(__engine).has_table('produtos'): 
            Base.metadata.create_all(bind=__engine)


if __name__ != '__main__':
    config_archive(database='loja', db_config_path=DB_CONFIG_PATH)
    load_dotenv(DB_CONFIG_PATH)