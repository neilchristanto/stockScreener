from infra import api
from infra.errors import api_error

class api_test():

  failCnt = 0
  failTst = []

  ###################################################
  def empty_ticker(self):
    print("...Testing empty ticker") 
    try:
      api.get_pd_df()
    except api_error as e:
      if e.msg != 'ticker not specified':
        self.failCnt += 1
        self.failTst.append('empty_ticker')

  ###################################################
  def ticker_default_period(self, ticker):
    print("...Testing get_pd_df for ticker {} with default period".format(ticker.upper()))
    df = api.get_pd_df(ticker)
    print(df)

  ###################################################
  def plot_ticker(self, ticker):
    print("...Testing plot ticker {} adjusted close for 1 year".format(ticker.upper()))
    df = api.get_pd_df(ticker, 'today', '-365')
    techInd = {"SMA": [10,50]}
    api.plot_chart(df['Adj Close'].sort_index(), '1 Year SPY', techInd=techInd)

  ###################################################
  def start_test(self):
    print("Starting api_test")
    self.empty_ticker()
    self.ticker_default_period('spy')
    self.plot_ticker('spy')

  def summary(self):
    print("Summary:")
    print("  failCnt = {}".format(self.failCnt))
    print("  failTst = {}".format(self.failTst))
