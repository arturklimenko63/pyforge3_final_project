import config
import logger
import postgres_connection
import get_json_data
import process_jsons
import reports

"""Instantiate of Logger"""
logger = logger.Logger(config.logger_file_name)

"""Instantiate of GetJsons class"""
json_data = get_json_data.GetData(config, logger)

"""Get data from number of urls specified in config.py"""
json_data.start_get_data()
if not json_data.is_any_responses_loaded():
    exit()

"""Instantiate of connection to Postgres"""
pg_connection = postgres_connection.PostgresEngine(config, logger)

"""Convert responses (jsons) into pandas data frames and store it into pg DB"""
process_data = process_jsons.ProcessJsonData(json_data.responses, config, pg_connection, logger)
process_data.process()

"""Report compounds"""
report = reports.Reports(config, pg_connection)
report.compounds_report()

