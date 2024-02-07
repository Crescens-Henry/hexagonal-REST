from user.infrastructure.MongoDB.mongo_db_repository import Repositorio as MongoRepositorio
from user.infrastructure.MYSQL.MYSQL_db_repository import Repositorio as MySQLRepositorio
from user.infrastructure.SQLite.SQLite_db_repository import Repositorio as SQLiteRepositorio

class RepositorioFactory:
    def __init__(self):
        self.repositorios = {
            "mongodb": MongoRepositorio(),
            "mysql": MySQLRepositorio(),
            "sqlite": SQLiteRepositorio()
        }

    def get_repositorio(self, db_type):
        return self.repositorios.get(db_type, None)
    