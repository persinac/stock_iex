import time
import numpy
import talib
import psycopg2
import sys
import requests
import logging
import math
import json
import os
from datetime import datetime
from pprint import pprint
from datetime import timedelta
from classes import HistoricalData

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root



if __name__ == '__main__':
    logging.basicConfig(filename=ROOT_DIR + '\example.log', level=logging.DEBUG)
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.debug("This is a test message")
    # https://cloud.iexapis.com/stable/stock/fsi/quote
    PARAMS = {'token': 'sk_9b0735e223214cffaf4def0848c833b7'}
    URL = "https://cloud.iexapis.com/stable/stock/fsi/quote"
    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    # extracting data in json format
    data = r.json()
    logger.debug(data)
    historicaldata = HistoricalData.HistoricalData(
        <parsed_values>
    )