from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('DB.HOST')
port = os.getenv('DB.PORT')

try:
    client = MongoClient(f"mongodb://{host}:{port}/")
    db = client['hecagonal_rest']
    print("Conexión exitosa a la base de datos")
except Exception as e:
    print(f"Error al conectar a la base de datos: {str(e)}")

