from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    load_dotenv()
    database = MongoClient(
        getenv("DB_URL"), tlsCAFile=where()
    )["Database"]

    def __init__(self, collection: str):
        self.collection = self.database[collection]

    def seed(self, amount):
        return self.collection.insert_many(
            [Monster().to_dict() for _ in range(amount)]
        ).acknowledged

    def reset(self):
        self.collection.delete_many({})

    def count(self) -> int:
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        cursor = self.collection.find({}, {'_id': False})
        df = DataFrame(list(cursor))
        return df

    def html_table(self) -> str:
        return self.dataframe().to_html()


if __name__ == '__main__':
    db = Database('xxx')
    db.seed(1000)

