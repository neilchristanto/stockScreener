class api_error(Exception):
  
  def __init__(self, funcName, msg):
    assert msg
    self.msg = msg
    self.funcName = funcName

  def __str__(self):
    retStr = "function: {};; errMsg {}".format(self.funcName, self.msg)
    return repr(retStr)
