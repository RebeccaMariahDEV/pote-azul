
from sqlalchemy import Column, Integer, String

from cliente.db_connection import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    telefone = Column(String)
    cpf = Column(String)

    def __repr__(self):
        return f'User {self.name}'

