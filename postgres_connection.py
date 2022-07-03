import sqlalchemy


class PostgresEngine:
    """Class to work with PostgreSQL"""

    def __init__(self, config, logger):
        """Class initialization"""

        try:
            self.host = config.host
            self.port = config.port
            self.db = config.db
            self.user = config.user
            self.password = config.password
            self.schema = config.schema
            self.conn = sqlalchemy.create_engine(
                f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}", echo=False)
            self.logger = logger
        except Exception as e:
            self.logger.error(f"PostgresEngine.__init__ failed. Error: {e}")
            raise

    """execute transaction"""
    def execute(self, execution_string):
        try:
            self.conn.execute(execution_string)
        except Exception as e:
            self.logger.error(f"PostgresEngine.execute failed. Error: {e}")
            raise
