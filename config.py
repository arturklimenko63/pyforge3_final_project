
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

"""Parameters to arrange parsing procedures"""
class Entity_config:
    table_name: str = 'compound'
    table_columns: [] = ['compound_id', 'name', 'formula', 'inchi', 'inchi_key', 'smiles', 'cross_links_count']
    record_path: [] = None
    customize_processing_function: str = 'parse_df'

"""Connection parameters to postgres DB"""
class Postgres_config:
    host = 'localhost'
    port = '5436'
    db   = 'postgres'
    user = 'postgres'
    password = 'diana'
    schema   = 'public'
