'''
Created on Oct 30, 2017

@author: dylanpowers
'''
from collections import Counter

'''
@param budget: amount of money available (integer).
@param people: file path to the file containing information about preferences.
@param drinks: file path to the file containing drinks and unit costs.
@param food: file path to the file containing food and unit costs.
@return: an array describing what should be bought for the party.
'''
def food_and_drink(budget, people, drinks, food):
    
    # If we do not have any money, we cannot buy anything.
    if budget <= 0:
        return 'You cannot buy anything.'
    
    # Open files for reading
    people = open(people,'r')
    drinks = open(drinks,'r')
    food = open(food,'r')
    
    costs, occur = generate_dicts(people, drinks, food)
    print costs
    print occur
    ppd = {}
    for k, v in occur.iteritems():
        ppd[k] = occur[k]/costs[k] # This is a dictionary representing the number of people pleased per $1 spent. This is how the algorithm chooses what to buy. 
    
    # Sort by the highest people-pleased-per-dollar values. This is an O(nlogn) operation.
    ppd = sorted(ppd.items(), key = lambda x: x[1]) 
    
    # This is what we will return - what we should buy
    buy = []
    
    for k, v in reversed(ppd): # We want highest values at the front
        if costs[k] <= budget:
            budget -= costs[k]
            print 'Buy ' + k + ' and your budget is now ' + str(budget) + '.'
            buy.append(k)
    
    return buy
''' 
Helper function to generate dictionaries for each of the three files.
    occur_c: generated from people_file, indicates how many people prefer each food/drink
    costs: generated from drinks_file and food_file, indicates costs of food and drink
'''
def generate_dicts(people_file, drinks_file, food_file):
    
    costs = {}
    occur = []
    for line in drinks_file:
        info = line.strip().split(':')
        costs[info[0]] = float(info[1]) # Add item is O(1) operation for dictionary; thus, entire loop is O(n) where n = number of drinks
        
    for line in food_file:
        info = line.strip().split(':')
        costs[info[0]] = float(info[1]) # Loop is O(m) where m is number of distinct food types
    
    mod = 1 # To keep track of which line we are at (person, food, or drink)
    for line in people_file:
        if mod%3 == 1: # This means that the current line is just a name - irrelevant to us
            mod += 1
            continue
        
        else: # At this point, we know that we are looking at food or drinks
            info = line.strip().split(',')
            for f_or_d in info:
                occur.append(f_or_d)
        mod += 1
    
    # collections.Counter will return a dictionary where keys are array entries and values are the number of times that they appear.
    occur_c = Counter(occur)
    return costs, dict(occur_c)