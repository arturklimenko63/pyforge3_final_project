import sqlalchemy
import json
import pandas as pd
import postgres_connection

class ProcessJsonData:
    def __init__(self, json_data, entity_config, postgres_config):
        """Class initialization"""
        self.json_data = json_data
        self.entity_config = entity_config
        self.postgres_config = postgres_config
        self.conn = postgres_connection.PostgresEngine(
            self.postgres_config.host, self.postgres_config.port,
            self.postgres_config.db, self.postgres_config.user,
            self.postgres_config.password, self.postgres_config.schema)

    def process(self):
        for i in self.json_data:
            json_data_tmp = json.loads(i)
            method = getattr(self, self.entity_config.customize_processing_function)
            if not method:
                raise NotImplementedError("Method %s not implemented" % self.entity_config.customize_processing_function)
            method(json_data_tmp)

    """this function is specified from config parameter. If we need to process more comple[ json we define another function"""
    def parse_df(self, json_data):
        parsed_df = pd.json_normalize(json_data, record_path=self.entity_config.record_path)
        compound_id = parsed_df.columns[0]
        parsed_df_transpose = parsed_df.transpose()
        tmp_dict = parsed_df_transpose.iloc[0][0]
        final_df = pd.DataFrame.from_dict(tmp_dict, orient='columns')
        for i in final_df.columns:
            if i not in self.entity_config.table_columns:
                if i == 'cross_links':
                    tmp_list = final_df.iloc[0][i]
                    cross_links_count = len(tmp_list)
                final_df.drop(i, axis=1, inplace=True)
        final_df.insert(0, 'compound_id', compound_id)
        final_df['cross_links_count'] = cross_links_count
        self.conn.upload_data_into_table(self.entity_config.table_name, final_df)
        print(compound_id)
