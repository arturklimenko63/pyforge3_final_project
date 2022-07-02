
"""List of compounds sources to obtain"""
urls = [
    'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/ATP',
    'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/ADP',
    'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/STI',
    'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/ZID',
    'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/DPM',
    'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/XP9',
    'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/18W',
    'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/29P'
]

"""Parameter to restrict number of http requests per second"""
requests_per_second = 1

"""Parameter how to usr Logger, if logger_file_name is not specified then output to console"""
logger_file_name = 'app.log'

"""section: Entity_config, parameters to arrange parsing procedures"""
table_name: str = 'compound'
table_columns: [] = ['compound_id', 'name', 'formula', 'inchi', 'inchi_key', 'smiles', 'cross_links_count']
record_path: [] = None
customize_processing_function: str = 'parse_df'

"""section: Postgres_config, vonnection parameters to postgres DB"""
host = 'localhost'
port = '5432'
db   = 'postgres'
user = 'test'
password = 'test'
schema   = 'public'

