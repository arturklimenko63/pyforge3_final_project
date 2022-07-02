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
            self.conn = sqlalchemy.create_engine(f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}", echo=False)
            self.logger = logger

            self.conn.execute(f"CREATE TABLE IF NOT EXISTS compound ( \
                                  compound_id varchar NOT NULL, \
                                  name varchar NOT NULL, \
                                  formula varchar NOT NULL, \
                                  inchi text NULL, \
                                  inchi_key varchar NULL, \
                                  smiles varchar NULL, \
                                  cross_links_count int4 NULL, \
                                CONSTRAINT compound_pkey PRIMARY KEY (compound_id))")
        except Exception as e:
            self.logger.error(f"PostgresEngine.__init__ failed. Error: {e}")
            raise


    def execute(self, execution_string):
        try:
            """execute transaction"""
            cur = self.conn.execute(execution_string)
        except Exception as e:
            self.logger.error(f"PostgresEngine.execute failed. Error: {e}")
            raise
