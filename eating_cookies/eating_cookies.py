#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  #base case
  #can't eat negative cookies
  if n < 0:
    return 0
  #there is only one way to eat 0 cookies
  if n == 0:
    return 1
  #count is equal to the sum of all possible ways to eat cookies
  count = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
  return count

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')