from contextlib import contextmanager

from singleton_decorator import singleton
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from settings import DB_URI

# Classe do SQLAlchemy para a declaração de tabelas
Base = declarative_base()


@singleton
# Decorador que faz com que essa classe seja carregada apenas uma vez, o singleton é um padrão de projeto
class DBConnector:
    def __init__(self):
        self.engine = create_engine(DB_URI, echo=True)
        self.session = scoped_session(sessionmaker(bind=self.engine))

    @contextmanager
    def conn_session(self):
        session = self.session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
