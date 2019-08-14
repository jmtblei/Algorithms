#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  #base case
  #if no ingredients, retun 0
  if len(ingredients) == 0:
    return 0
  #keep a count of how many batches we can make
  count = 0
  #check the number of ingredients
  while len(ingredients) > 0:
    #subtract the recipe amount from ingredients on hand. if not enough ingredients, we can't make a batch so return the count
    for i in recipe.items():
      if i in ingredients:
        if ingredients[i] - recipe[i] < 0:
          return count
        #if we have enough ingredients, subtract the required recipe amount from ingredients on hand
        else:
          ingredients[i] = ingredients[i] - recipe[i]
      #else we dont have enough ingredients, return 0
      else:
        return 0  
    #increase the count
    count += 1
  #return the count
  return count

  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))