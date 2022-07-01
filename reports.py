import pandas as pd

class Reports():
    def __init__(self, pg_connection):
        """Class initialization"""

        self.pg_connection = pg_connection
        self.pg_connection.execute(f"CREATE OR REPLACE VIEW v_compaund \
                            as \
                            SELECT compound_id, \
                                   CASE \
                                     WHEN length(name) > 10 THEN \
                                       substr(name, 1, 10) || '...' \
                                     ELSE  \
                                       name \
                                   END AS name, \
                                   CASE  \
                                     WHEN length(formula) > 10 THEN \
                                       substr(formula, 1, 10) || '...' \
                                     ELSE  \
                                       formula \
                                   END AS formula, \
                                   CASE  \
                                     WHEN length(inchi) > 10 THEN \
                                       substr(inchi, 1, 10) || '...' \
                                     ELSE  \
                                       inchi \
                                   END AS inchi, \
                                   CASE  \
                                     WHEN length(inchi_key) > 10 THEN \
                                       substr(inchi_key, 1, 10) || '...' \
                                     ELSE  \
                                       inchi_key \
                                   END AS inchi_key, \
                                   CASE  \
                                     WHEN length(smiles) > 10 THEN \
                                       substr(smiles, 1, 10) || '...' \
                                     ELSE  \
                                       smiles \
                                   END AS smiles, \
                                   cross_links_count \
                              FROM compound")

#    def compounds_report(self):
#        self.pg_connection.compounds_report()

    def compounds_report(self):
        df = pd.read_sql("select * from v_compaund", self.pg_connection.conn)
        print(df.to_markdown())
