from datetime import date
from datetime import timedelta
from urllib import request as req

from .errors import api_error

import pandas as pd

"""
Get CSV file from Yahoo
The URL has the month starting from 0-11
So the month is offset by -1

Input:
  ticker    : stock symbol
  endDate   : choices:
                - 'today'
                - 'YYYY-MM-DD'
  startDate : choices:
                - days delta (e.g. '-30')
                - 'YYYY-MM-DD'

Output:
  pandas dataFrame
"""
def get_pd_df(ticker=None, endDate='today', startDate='-30'):
  if ticker == None:
    raise api_error('get_pd_df', 'ticker not specified')

  # determine end period
  if endDate == 'today':
    bYear   = date.today().year
    bMonth  = date.today().month - 1
    bDate   = date.today().day
  else:
    bYear, bMonth, bDate = endDate.split('-')

  # determine start period
  if startDate[0] == '-':
    aTemp   = date.today() + timedelta(days=int(startDate))
    aYear   = aTemp.year
    aMonth  = aTemp.month - 1
    aDate   = aTemp.day
  else:
    aYear, aMonth, aDate = startDate.split('-')
  
  # get CSV from Yahoo
  url = "http://chart.finance.yahoo.com/table.csv?s={}&a={}&b={}&c={}&d={}&e={}&f={}&g=d&ignore=.csv".\
    format(ticker.upper(), aMonth, aDate, aYear, bMonth, bDate, bYear)
 
  try:
    retVal = pd.read_csv(url, index_col='Date', parse_dates=True)
  except:
    raise api_error('get_pd_df', 'url {} can\'t be opened'.format(url))

  return retVal
