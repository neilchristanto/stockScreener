from infra import api
from infra.errors import api_error

class api_test():

  failCnt = 0
  failTst = []

  def empty_ticker(self):
    print("...Testing empty ticker") 
    try:
      api.get_csv()
    except api_error as e:
      if e.msg != 'ticker not specified':
        self.failCnt += 1
        self.failTst.append('empty_ticker')

  def start_test(self):
    print("Starting api_test")
    self.empty_ticker()

  def summary(self):
    print("Summary:")
    print("  failCnt = {}".format(self.failCnt))
    print("  failTst = {}".format(self.failTst))
