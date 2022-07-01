from get_json_data import GetData
import config
from logger import Logger

import pytest


@pytest.mark.asyncio
async def test_get_data_by_url_right():
    logger = Logger(config.logger_file_name)
    json_data = GetData(config, logger)
    json_data.requests_per_second = 1
    json_data.urls = ['https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/ATP']
    json_data.responses = []

    await json_data.get_data_by_url(None, 'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/ATP')
    assert json_data.responses[0].find("ATP") != -1


@pytest.mark.asyncio
async def test_get_data_by_url_wrong():
    logger = Logger(config.logger_file_name)
    json_data = GetData(config, logger)
    json_data.requests_per_second = 1
    json_data.urls = ['http://sdfssg']
    json_data.responses = []

    await json_data.get_data_by_url(None, 'http://sdfssg')
    assert len(json_data.responses) == 0

@pytest.mark.asyncio
async def test_get_data_by_url_empty_url():
    logger = Logger(config.logger_file_name)
    json_data = GetData(config, logger)
    json_data.requests_per_second = 1
    json_data.urls = ['']
    json_data.responses = []

    await json_data.get_data_by_url(None, '')
    assert len(json_data.responses) == 0
