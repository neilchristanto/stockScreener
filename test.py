from tests.api_test import api_test

def main():
  tst = api_test()
  tst.start_test()
  tst.summary()

if __name__ == "__main__":
  main()
