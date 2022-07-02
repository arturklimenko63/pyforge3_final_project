import asyncio
import requests

from utils import tic


class GetData:
    """Class to obtain jsons from https://www.ebi.ac.uk"""

    def __init__(self, config, logger):
        """Class initialization"""
        self.urls = config.urls
        self.requests_per_second = config.requests_per_second
        self.logger = logger

    """Put data from url into array"""
    responses = []

    async def get_data_by_url(self, ioloop, Url):
        try:
            self.logger.info(f"getting data from {Url} started: {format(tic())}")
            response = requests.get(Url)
            if response.status_code == 200:
                self.responses.append(response.text)
                v_result = 0
            else:
                v_result = -1
            await asyncio.sleep(self.requests_per_second)
            self.logger.info(f"getting data from {Url} finished: {format(tic())}")
            return v_result
        except Exception as e:
            self.logger.error(f"get_data_by_url failed. Error: {e}")
            return -1

    def start_get_data(self):
        ioloop = asyncio.get_event_loop()
        tasks = [self.get_data_by_url(ioloop, i) for i in self.urls]
        ioloop.run_until_complete(asyncio.wait(tasks))
        ioloop.close()


    def is_any_responses_loaded(self):
        return len(self.responses) > 0