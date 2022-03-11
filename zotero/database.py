import sqlite3


class DatabaseInterface:
    def __ini__(self, path: str) -> None:
        self.path = path
