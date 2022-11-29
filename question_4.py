#Group 11D
#Laurence Perreault, Zachary Quirion-Haddine, Jerry
#Presentation Exercise 4

import random

### Import ingredient  and noun lists from file ingredients.txt and nouns.txt ###
open_file = open("ingredients.txt", "r")
file_content = open_file.read()
INGREDIENTS_LIST = file_content.split("\n")
open_file.close()

open_file = open("nouns.txt", "r")
file_content = open_file.read()
NOUNS_LIST = file_content.split("\n")
open_file.close()


class Chef:
    """     """
    
    def __init__(self, name, record, cuisine):
        self.name = name
        self.record = record
        self.cuisine = cuisine
        
    def __str__(self):
        return self.name
        
class Dish:
    """     """
    
    def __init__(self, name, ingredients, chef, ratings=[0, 0, 0, 0]):
        """
        """
        self.name = name
        self.ingredients = ingredients
        self.chef = chef
        self.ratings = ratings
        
    def __str__(self):
        return self.name
        
    def rate_dish(self):
        """
        """
        for i in range(4):
            self.ratings[i] = random.randint(1,10)

class Battle:
    """       """
    def __init__(self, iron_chef, challenger, secret_ingredient, dishes=[], outcome=""):
        """
        """
        self.iron_chef = iron_chef
        self.challenger = challenger
        self.secret_ingredient = secret_ingredient
        self.dishes = dishes
        self.outcome = outcome

    def conclude(self):
        """
        """
        
        iron_chef_score = 0
        challenger_score = 0
        
        for plate in self.dishes:
            plate.rate_dish()
            
            if plate.chef == self.iron_chef:
                iron_chef_score += sum(plate.ratings)
            else:
                challenger_score += sum(plate.ratings)
        
        if iron_chef_score > challenger_score:
            self.outcome = "iron_chef"
        elif iron_chef_score == challenger_score:
            self.outcome = "tie"
        else:
            self.outcome = "challenger"

class KitchenStadium:
    """      """
    def __init__(self, iron_chefs, challengers, ingredients, battles):
        """
        """
        self.iron_chefs = iron_chefs
        self.challengers = challengers
        self.ingredients = ingredients
        self.battles = battles

    def get_top_chef(self):
        """
        """
        
    def get_best_dishes(self):
        """
        """
    
    def run_battle(self, iron_chef, challenger):
        """
        """
        ### My suggestion: I have imported two lists, one for ingredients and one for nouns in the form of "NOUN of " 
        ### so that you can concatenate it with the name of the secret ingredient. For example, the random name we give to 
        ### a dish could be "Flavour of cherry", where cherry is the secret ingredient randomly chosen, and the randomly 
        ### chosen noun is "Flavour of". Just remember to not have the same name repeat.
        ### Do print(NOUNS_LIST) and print(INGREDIENTS_LIST) to see the two lists I've imported.
        ### >>> print(NOUNS_LIST[0] + INGREDIENTS_LIST[0])
        ### >>> "Piety of cocoa powder"
        ###
        ### >>> print(NOUNS_LIST[112] + INGREDIENTS_LIST[68])
        ### >>> "Judgement of dandelion"












### Testing ###

# iron = Chef("Alex", (1, 2, 3), "American")
# chal = Chef("Steph", (1, 2, 3), "English")
# 
# CHEFS = iron, chal
# dish_list = []
# 
# for j in range(10):
#     choose_chef = CHEFS[random.randint(0,1)] #Issue using random.choices to directly choose from CHEFS tuple
# 
#     choose_dish = Dish("test", ["ingredient_1", "ingredient_2"], choose_chef)
#     dish_list.append(choose_dish)
# 
# while True:
#     test_Battle = Battle(iron, chal, "potatoes", dish_list)
#     test_Battle.conclude()
#     print(test_Battle.outcome)
#     if test_Battle.outcome == "tie":
#         break
# 


# new_Dish = Dish("Poutine", ["ingredient_1", "ingredient_2"], new_Chef)
# new_Dish.rate_dish()
# print(new_Dish.ratings)




