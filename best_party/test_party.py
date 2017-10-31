'''
Created on Oct 31, 2017

@author: dylanpowers
'''
import unittest
from party_specs import food_and_drink

class Test(unittest.TestCase):

    # Normal test case
    def test_normal_case(self):
        self.assertEqual(food_and_drink(5, 'data/people.txt', 'data/drinks.txt','data/food.txt'), ['water','tortillachips','kettlechips'])
        self.assertEqual(food_and_drink(10, 'data/people.txt', 'data/drinks.txt','data/food.txt'), ['water','tortillachips','kettlechips', 'gingerale'])
        self.assertEqual(food_and_drink(20, 'data/people.txt', 'data/drinks.txt','data/food.txt'), ['water','tortillachips','kettlechips', 'gingerale','fritos','lemonade'])
    
    # The following tests that the program doesn't always buy the product with the highest people pleased per dollar - 
    # in some cases, it won't have enough money to do that, but can please some other people by buying a cheaper item.
    def test_low_budget(self):
        self.assertEqual(food_and_drink(1, 'data/low_budget_people.txt', 'data/low_budget_drinks.txt','data/low_budget_food.txt'), ['coke'])
        
    # Negative budget
    def test_negative_budget(self):
        self.assertEqual(food_and_drink(-1, 'data/people.txt','data/drinks.txt','data/food.txt'), 'You cannot buy anything.')

if __name__ == "__main__":
    unittest.main()