import datetime

def get_timestamp():
  now = datetime.datetime.now()
  return now.strftime('%Y_%m_%d_%H_%M_%S')
