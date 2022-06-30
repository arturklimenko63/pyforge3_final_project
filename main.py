import config
import get_json_data
import process_jsons

"""Instantiate of GetJsons class"""
json_data = get_json_data.GetData(config)

"""Get data from number of urls specified in config.py"""
json_data.startGetData()

"""Pick compounds"""
json_data = json_data.responses

"""Convert responses (jsons) into pandas data frames and store it into pg DB"""
process_data = process_jsons.ProcessJsonData(json_data, config.Entity_config, config.Postgres_config)
process_data.process()


