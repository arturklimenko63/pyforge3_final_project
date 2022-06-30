import sqlalchemy
import pandas as pd

class PostgresEngine:
    """Class to work with PostgreSQL"""

    def __init__(self, host, port, db, user, password, schema):
        """Class initialization"""
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        self.schema = schema
        self.conn = sqlalchemy.create_engine(f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}", echo=True)
        #self.conn.execute(f"DROP TABLE if exists public.compound")

    def execute(self, execution_string):
        """execute transaction"""
        cur = self.conn.execute(execution_string)

    def upload_data_into_table(self, table_name, input_df: pd.DataFrame):
        """insert dataframe into the postgres table"""
        try:
            """to_sql "insert" approach"""
            input_df.to_sql(table_name, con=self.conn, index=False, if_exists='append')
        except Exception as e:
            print(f"to_sql failed. Error: {e}")
            raise
