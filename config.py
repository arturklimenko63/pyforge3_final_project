
"""Url of compounds source"""
url = 'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/'

"""List of compounds to obtain"""
compounds = ['ATP', 'ADP', 'STI', 'ZID', 'DPM', 'XP9', '18W', '29P']

"""Parameter to restrict number of http requests per second"""
requests_per_second = 1

"""Parameter how to usr Logger, if logger_file_name is not specified then output to console"""
#logger_file_name = 'app.log'
logger_file_name = ''

"""section: Entity_config, parameters to arrange parsing procedures"""
table_name: str = 'compound'
table_columns: [] = ['compound_id', 'name', 'formula', 'inchi', 'inchi_key', 'smiles', 'cross_links_count']
record_path: [] = None
customize_processing_function: str = 'parse_and_upload_df'

"""section: Postgres_config, connection parameters to postgres DB"""
host = 'localhost'
port = '5432'
db   = 'postgres'
user = 'test'
password = 'test'
schema   = 'public'

table_ddl = "CREATE TABLE IF NOT EXISTS compound ( \
                 compound_id varchar NOT NULL, \
                 name varchar NOT NULL, \
                 formula varchar NOT NULL, \
                 inchi text NULL, \
                 inchi_key varchar NULL, \
                 smiles varchar NULL, \
                 cross_links_count int4 NULL, \
                 CONSTRAINT compound_pkey PRIMARY KEY (compound_id))"

"""section: Reports"""
view_ddl = "CREATE OR REPLACE VIEW v_compound \
                                as \
                                SELECT compound_id, \
                                       CASE \
                                         WHEN length(name) > 13 THEN \
                                           substr(name, 1, 10) || '...' \
                                         ELSE  \
                                           name \
                                       END AS name, \
                                       CASE  \
                                         WHEN length(formula) > 13 THEN \
                                           substr(formula, 1, 10) || '...' \
                                         ELSE  \
                                           formula \
                                       END AS formula, \
                                       CASE  \
                                         WHEN length(inchi) > 13 THEN \
                                           substr(inchi, 1, 10) || '...' \
                                         ELSE  \
                                           inchi \
                                       END AS inchi, \
                                       CASE  \
                                         WHEN length(inchi_key) > 13 THEN \
                                           substr(inchi_key, 1, 10) || '...' \
                                         ELSE  \
                                           inchi_key \
                                       END AS inchi_key, \
                                       CASE  \
                                         WHEN length(smiles) > 13 THEN \
                                           substr(smiles, 1, 10) || '...' \
                                         ELSE  \
                                           smiles \
                                       END AS smiles, \
                                       cross_links_count \
                                  FROM compound"

view_select = "select * from v_compound"
