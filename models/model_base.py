'''Model Base to create ORM tables with SQL Alchemy'''
from sqlalchemy.orm import declarative_base
from conf.session_db import __engine


Base = declarative_base(bind=__engine)

if __name__ == '__main__':
    print(__doc__)