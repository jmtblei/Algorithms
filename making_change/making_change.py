#!/usr/bin/python

import sys

def making_change(amount, denominations):
  #base case
  #What should happen when the amount of cents given is 0?
  #if amount is 0, there is only 1 way to denominate change
  if amount == 0:
    return 1
  #What should happen when the amount of cents given is negative?
  #if amount is less than 0, there is no way to denominate the change 
  if amount < 0:
    return 0
  #What about when we've used up all of the available coin denominations?
  #if denominations is 0, there is no way to denominate change
  if len(denominations) == 0:
    return 0
  #changing out will be the sum of both counts for possible ways to make change
  return making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[:-1])


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")