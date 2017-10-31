'''
Created on Oct 30, 2017

@author: dylanpowers
'''
import unittest
from collections import Counter

def food_and_drink(budget):
    
    people = open('data/people.txt','r')
    drinks = open('data/drinks.txt','r')
    food = open('data/food.txt','r')
    
    costs, occur = generate_dicts(people, drinks, food)
    ppd = {}
    for k, v in occur.iteritems():
        ppd[k] = occur[k]/costs[k]
    
    ppd = sorted(ppd.items(), key = lambda x: x[1])
    print ppd
    for k, v in reversed(ppd):
        budget -= costs[k] * occur[k]
        print 'budget is now ' + str(budget)
        if budget < 0: break
        print 'Buy ' + k
''' 
Helper function to generate dictionaries for each of the three files.
    people_dict: keys are names (with _1, _2, etc if they are non-unique), and values are food and drink preferences
    drink_dict: keys are drinks, values are unit prices
    foods_dict: keys are foods, values are unit prices
'''
def generate_dicts(people_file, drinks_file, food_file):
    mod = 1 # To keep track of which line we are at (person, food, or drink)
    
    costs = {}
    occur = []
    for line in drinks_file:
        info = line.strip().split(':')
        costs[info[0]] = float(info[1]) # Add item is O(1) operation for dictionary; thus, entire loop is O(n) where n = number of drinks
        
    for line in food_file:
        info = line.strip().split(':')
        costs[info[0]] = float(info[1]) # Loop is O(m) where m is number of distinct food types
    
    for line in people_file:
        if mod%3 == 1: # This means that the current line is just a name - irrelevant to us
            mod += 1
            continue
        
        else: # At this point, we know that we are looking at food or drinks
            info = line.strip().split(',')
            for f_or_d in info:
                occur.append(f_or_d)
        mod += 1
    
    occur_c = Counter(occur)
    return costs, dict(occur_c)
    
if __name__ == '__main__':
    
    food_and_drink(100)
