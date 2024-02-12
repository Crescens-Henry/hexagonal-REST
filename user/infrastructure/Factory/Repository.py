from user.infrastructure.repositories.MYSQL_db_repository import Repositorio as MySQLRepositorio
from user.infrastructure.repositories.SQLite_db_repository import Repositorio as SQLiteRepositorio

class RepositorioFactory:
    def __init__(self):
        self.repositorios = {
            "mysql": MySQLRepositorio(),
            "sqlite": SQLiteRepositorio()
        }

    def get_repositorio(self, db_type):
        return self.repositorios.get(db_type, None)
    