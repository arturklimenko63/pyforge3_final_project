import json
import pandas as pd

class ProcessJsonData:
    def __init__(self, json_data, config, pg_connection, logger):
        """Class initialization"""
        self.json_data = json_data
        self.config = config
        self.logger = logger
        self.pg_connection = pg_connection

    def process(self):
        try:
            for i in self.json_data:
                json_data_tmp = json.loads(i)
                method = getattr(self, self.config.customize_processing_function)
                if not method:
                    self.logger.error("Method %s not implemented" % self.config.customize_processing_function)
                    raise NotImplementedError("Method %s not implemented" % self.config.customize_processing_function)
                method(json_data_tmp)
        except Exception as e:
            self.logger.error(f"ProcessJsonData.process failed. Error: {e}")
            raise

    """this function is specified from config parameter. If we need to process more comple[ json we define another function"""
    def parse_df(self, json_data):
        try:
            parsed_df = pd.json_normalize(json_data, record_path=self.config.record_path)
            compound_id = parsed_df.columns[0]
            parsed_df_transpose = parsed_df.transpose()
            tmp_dict = parsed_df_transpose.iloc[0][0]
            final_df = pd.DataFrame.from_dict(tmp_dict, orient='columns')
            for i in final_df.columns:
                if i not in self.config.table_columns:
                    if i == 'cross_links':
                        tmp_list = final_df.iloc[0][i]
                        cross_links_count = len(tmp_list)
                    final_df.drop(i, axis=1, inplace=True)
            final_df.insert(0, 'compound_id', compound_id)
            final_df['cross_links_count'] = cross_links_count
            self.upload_data_into_table(self.config.table_name, final_df)
            self.logger.info(f"compound_id: {compound_id} loaded into '{self.config.table_name}' table.")
        except Exception as e:
            self.logger.error(f"ProcessJsonData.parse_df failed. Error: {e}")
            raise

    def upload_data_into_table(self, table_name, input_df: pd.DataFrame):
        """insert dataframe into the postgres table"""
        try:
            """to_sql "insert" approach"""
            input_df.to_sql(table_name, con=self.pg_connection.conn, index=False, if_exists='append')
        except Exception as e:
            self.logger.error(f"to_sql failed. Error: {e}")
            raise
