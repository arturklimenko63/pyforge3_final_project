import pandas as pd


class Reports():
    """Class to work with reports"""

    def __init__(self, config, pg_connection):
        """Class initialization"""

        try:
            self.pg_connection = pg_connection
            self.pg_connection.conn.execute(config.view_ddl)
        except Exception as e:
            self.logger.error(f"Reports.__init__ failed. Error: {e}")
            raise

    def compounds_report(self):
        df = pd.read_sql("select * from v_compound", self.pg_connection.conn)
        print(df.to_markdown())
