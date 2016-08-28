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
    print("...Testing ticker {} with default period".format(ticker.upper()))
    csv = api.get_pd_df(ticker)
    print(csv)

  def start_test(self):
    print("Starting api_test")
    self.empty_ticker()
    self.ticker_default_period('spy')

  def summary(self):
    print("Summary:")
    print("  failCnt = {}".format(self.failCnt))
    print("  failTst = {}".format(self.failTst))
