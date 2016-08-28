import time as _time
from .errors import api_error

"""
Get CSV file from Yahoo
  ticker    : stock symbol
  endDate   : choices:
                - 'today'
                - 'YYYY-MM-DD'
  startDate : choices:
                - days delta (e.g. '-30')
                - 'YYYY-MM-DD'
"""
def get_csv(ticker=None, endDate='today', startDate='-30'):
  if ticker == None:
    raise api_error('get_csv', 'ticker not specified')
