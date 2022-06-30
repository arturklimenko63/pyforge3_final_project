from utils import tic
import asyncio
import requests
import logging

class GetData:
    """Class to obtain jsons from https://www.ebi.ac.uk"""

    def __init__(self, config):
        """Class initialization"""
        self.urls = config.urls
        self.requests_per_second = config.requests_per_second

    responses = []

    async def getDataByUrl(self, ioloop, Url):
        print(f"getting data from  {Url} started: {format(tic())}")
        response = requests.get(Url)
        self.responses.append(response.text)
        await asyncio.sleep(self.requests_per_second)
        print(f"getting data from Url: {Url} finished: {format(tic())}")

    def startGetData(self):
        ioloop = asyncio.get_event_loop()
        tasks = [self.getDataByUrl(ioloop, i) for i in self.urls]
        ioloop.run_until_complete(asyncio.wait(tasks))
        ioloop.close()
