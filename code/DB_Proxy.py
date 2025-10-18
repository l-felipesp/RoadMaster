# code/DB_Proxy.py
import sqlite3
from typing import List, Tuple, Dict


class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self._ensure_schema()

    def _ensure_schema(self) -> None:
        cur = self.connection.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS dados(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL,
                date TEXT NOT NULL
            )
            """
        )
        self.connection.commit()

    def save(self, score_dict: Dict[str, object]) -> None:
        #Espera um dicionário com chaves 'name','score','date'.

        cur = self.connection.cursor()
        cur.execute(
            "INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)",
            {"name": score_dict["name"], "score": int(score_dict["score"]), "date": score_dict["date"]},
        )
        self.connection.commit()

    def retrieve_top10(self) -> List[Tuple[int, str, int, str]]:
        #Retorna lista de tuplas (id, name, score, date) ordenadas por score desc, limite de 10.

        cur = self.connection.cursor()
        rows = cur.execute("SELECT * FROM dados ORDER BY score DESC LIMIT 10").fetchall()
        return rows

    def close(self) -> None:
        if self.connection:
            self.connection.close()
            self.connection = None
