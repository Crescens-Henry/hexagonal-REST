from mongoengine import connect
import os
from dotenv import load_dotenv

class DBConnection:
    def __init__(self):
        load_dotenv()

        host = os.getenv('DB.HOST')
        port = os.getenv('DB.PORT')

        try:
            connect(db='hexagonal_rest', host=host, port=int(port))
            print("Conexión exitosa a la base de datos")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {str(e)}")
