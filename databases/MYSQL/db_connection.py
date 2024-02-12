from sqlalchemy import DateTime
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

Base = declarative_base()
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    cellphone = Column(String(20), nullable=False, unique=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    token_uuid = Column(String(36), unique=True)
    verified = Column(Boolean, default=False)
    verified_at = Column(DateTime)
    
    
class DBConnection:
    def __init__(self):
        load_dotenv()

        host = os.getenv('DB.HOST_MYSQL')
        port = os.getenv('DB.PORT_MYSQL')
        user = os.getenv('DB.USER_MYSQL')
        password = os.getenv('DB.PASSWORD_MYSQL')
        database = os.getenv('DB.DATABASE_MYSQL')

        try:
            self.engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
            Base.metadata.create_all(self.engine)
            self.Session = sessionmaker(bind=self.engine)
            print("Conexión exitosa a la base de datos con MySQL LISTA!")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {str(e)}")