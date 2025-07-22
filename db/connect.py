from .config import Config 
import psycopg2

class DB(Config):
    def __init__(self, **kwargs):
        super().__init__()

        self.connect = psycopg2.connect(
            dbname=self.DB_NAME,
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
        )
        self.cur = self.connect.cursor()
        
        self.kwargs = kwargs



    def insert(self):
        col = " , ".join(self.kwargs.keys())
        value = " , ".join(["%s"] * len(self.kwargs.keys()))

        query = f"""insert into {self.__class__.__name__.lower()} ({col}) values ({value});"""

        params = tuple(self.kwargs.values())

        self.cur.execute(query, params)
        self.connect.commit()

    def delete(self, conditions : str = ''):
        if not conditions:
            query = f""" delete from {self.__class__.__name__.lower()}; """
        else:
            query = f"""delete from {self.__class__.__name__.lower()} where {conditions} """

        self.cur.execute(query)
        self.connect.commit()

    def update(self, conditions, **set_value):

        new_values = " = %s, ".join(set_value.keys()) + " = %s"
        query = f"""update {self.__class__.__name__.lower()} set {new_values} where {conditions};"""
        params = tuple(set_value.values())
        self.cur.execute(query, params)
        self.connect.commit()

    def select(self,  condition = '', columns = '*'):

        if not condition:
            query = f"""select {columns} from {self.__class__.__name__.lower()};"""
        else:
            query = f"""select {columns} from {self.__class__.__name__.lower()} where {condition};"""
        self.cur.execute(query)
        return self.cur.fetchall()