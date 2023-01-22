import time

# This function is a decorator. It measures the time it takes a function to run and prints it to the console.
def time_it(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(func.__name__ + ' took ' + str((end-start) * 1000) + ' mil sec')
    return result
  return wrapper