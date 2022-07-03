import pandas as pd


class Reports:
    """Class to work with reports"""

    def __init__(self, config, logger, pg_connection):
        """Class initialization"""

        self.config = config
        self.logger = logger
        self.pg_connection = pg_connection

    def compounds_report(self):
        try:
            """Check if view_ddl exists"""
            self.pg_connection.conn.execute(self.config.view_ddl)
            df = pd.read_sql(self.config.view_select, self.pg_connection.conn)
            print(df.to_markdown())
        except Exception as e:
            self.logger.error(f"Reports.__init__ failed. Error: {e}")
            raise

