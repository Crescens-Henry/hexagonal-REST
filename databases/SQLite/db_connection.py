from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

Base = declarative_base()
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)

class DBConnection:
    def __init__(self):
        load_dotenv()

        database_path = os.getenv('DB.PATH_SQLITE')

        try:
            self.engine = create_engine(f'sqlite:///{database_path}')
            Base.metadata.create_all(self.engine)
            self.Session = sessionmaker(bind=self.engine)
            print("Conexión exitosa a la base de datos con SQLite LISTA!")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {str(e)}")