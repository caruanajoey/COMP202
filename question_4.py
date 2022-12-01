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
    """
    This class represents the characteristics of a chef.
    Attributes: name, record, cuisine
    """
    
    def __init__(self, name, record, cuisine):
        
        self.name = name
        self.record = record
        self.cuisine = cuisine
        
    def __str__(self):
        
        wins = self.record[0]
        losses = self.record[1]
        ties = self.record[2]
        
        print("name: "+self.name)
        print("wins: "+str(wins))
        print("losses: "+str(losses))
        print("ties: "+str(ties))
        print("cuisine: "+self.cuisine)
        
class Dish:
    """ 
    This class represents the characteristics of a dish.
    Attributes: name, ingredients, chef, ratings
    """
    
    def __init__(self, name, ingredients, chef, ratings=[0,0,0,0]):
       
        self.name = name
        self.ingredients = ingredients
        self.chef = chef
        self.ratings = ratings
        
    def __str__(self):
        
        print("name of dish: "+self.name)
        for i in self.ingredients:
            print("ingredient: "+i)
        print("chef: "+ self.chef.name)
        print("ratings: "+ str(self.ratings))
        
    def rate_dish(self):
        """
        (Dish)->list<int>
        This function randomly attributes 4 notes between 1 and 10. It returns the new ratings of the dish.
        >>>random.seed(11)
        >>>lasagna = Dish("lasagna",[],Lydia,[0,0,0,0])
        >>>Dish.rate_dish(lasagna)
        [8,9,8,8]
        >>>random.seed(15)
        >>>lasagna = Dish("lasagna",[],Lydia,[0,0,0,0])
        >>>Dish.rate_dish(lasagna)
        [4,1,9,1]
        >>>random.seed(16)
        >>>cake = Dish("Carrot cake",[],Lydia,[0,0,0,0])
        >>>Dish.rate_dish(cake)
        [6,8,8,5]
        """
        for i in range(4):
            self.ratings[i] = random.randint(1,10)
        
        return self.ratings

class Battle:
    """  
    This class represents the characteristics of a battle.
    Attributes: iron chef, challenger, secret ingredient, dishes, outcome
    """
    def __init__(self, iron_chef, challenger, secret_ingredient, dishes, outcome=""):
        
        self.iron_chef = iron_chef
        self.challenger = challenger
        self.secret_ingredient = secret_ingredient
        self.dishes = dishes
        self.outcome = outcome
    
    def __str__(self):
        
        print("iron chef: "+self.iron_chef.name)
        print("challenger chef: "+self.challenger.name)
        print("secret ingredient: "+self.secret_ingredient)
        for i in self.dishes:
            print("dish: "+i.name)
        print("outcome: "+self.outcome)

    def conclude(self):
        """
        (Battle)-> str
        This functions randomly attributes 4 notes between 1 and 10 to each dish that was prepared during the battle.
        It adds up the notes and returns the chef with the highest score. In case of a tie, it returns "tie".
        >>> random.seed(11)
        >>> Battle1 = Battle(Lydia,Bob,"tomato",[lasagna,pizza],"")
        >>> Battle.conclude(Battle1)
        'iron_chef'
        >>> random.seed(18)
        >>> Battle1 = Battle(Lydia,Bob,"tomato",[lasagna,pizza],"")
        >>> Battle.conclude(Battle1)
        'challenger'
        >>> random.seed(78)
        >>> Battle3 = Battle(Joe,Bob,"carrot", [sauté,salad],"")
        >>> Battle.conclude(Battle3)
        'challenger'
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
        
        return self.outcome

class KitchenStadium:
    """ 
    This class represents the characteristics of a Kitchen Stadium.
    Attributes: iron chefs, challengers, ingredients, battles
    """
    def __init__(self, iron_chefs, challengers, ingredients, battles):
        
        self.iron_chefs = iron_chefs
        self.challengers = challengers
        self.ingredients = ingredients
        self.battles = battles
        
    def __str__(self):
        
        for i in self.iron_chefs:
            print("chef: "+i.name)
        for i in self.challengers:
            print("challenger: "+i.name)
        for i in self.ingredients:
            print("ingredient: "+i)
        print("number of battles: "+str(len(self.battles)))

    def get_top_chef(self):
        """
        (KitchenStadium)->Chef
        This functions returns the chef that has the best rating, meaning the ratio between the won battles and the total of battles that were played
        by this chef.
        >>>Lydia = Chef("Lydia",(1,2,3),"French")
        >>>Bob = Chef("Bob",(1,2,4), "Japanese")
        >>>lasagna = Dish("lasagna",[],Lydia,[0,0,0,0])
        >>>pizza = Dish("pizza",[],Bob,[0,0,0,0])
        >>>soup = Dish("soup",[],Lydia,[0,0,0,0])
        >>>sauté = Dish("sauté",[],Bob,[0,0,0,0])
        >>>cake = Dish("Carrot cake",[],Lydia,[0,0,0,0])
        >>>salad = Dish("salad",[],Bob,[0,0,0,0])
        >>>Battle1 = Battle(Lydia,Bob,"tomato",[lasagna,pizza],"")
        >>>Battle2 = Battle(Lydia,Bob,"mushroom",[soup,sauté],"")
        >>>Battle3 = Battle(Lydia,Bob,"carrot", [cake,salad],"")
        >>>kitchen = KitchenStadium([Lydia],[Bob],INGREDIENTS_LIST,[Battle1,Battle2,Battle3])
        >>>KitchenStadium.get_top_chef(kitchen)
        Lydia
        >>>Lydia = Chef("Lydia",(1,2,3),"French")
        >>>Bob = Chef("Bob",(1,2,4), "Japanese")
        >>>Joe = Chef("Joe",(4,5,6),"Italian")
        >>>lasagna = Dish("lasagna",[],Lydia,[0,0,0,0])
        >>>pizza = Dish("pizza",[],Bob,[0,0,0,0])
        >>>soup = Dish("soup",[],Lydia,[0,0,0,0])
        >>>sauté = Dish("sauté",[],Joe,[0,0,0,0])
        >>>cake = Dish("Carrot cake",[],Lydia,[0,0,0,0])
        >>>salad = Dish("salad",[],Bob,[0,0,0,0])
        >>>Battle1 = Battle(Lydia,Bob,"tomato",[lasagna,pizza],"")
        >>>Battle2 = Battle(Lydia,Joe,"mushroom",[soup,sauté],"")
        >>>Battle3 = Battle(Joe,Bob,"carrot", [sauté,salad],"")
        >>>kitchen = KitchenStadium([Lydia],[Bob,Joe],INGREDIENTS_LIST,[Battle1,Battle2,Battle3])
        >>>KitchenStadium.get_top_chef(kitchen)
        Joe 
        >>>Lydia = Chef("Lydia",(1,2,3),"French")
        >>>Bob = Chef("Bob",(1,2,4), "Japanese")
        >>>Joe = Chef("Joe",(4,5,6),"Italian")
        >>>lasagna = Dish("lasagna",[],Lydia,[0,0,0,0])
        >>>pizza = Dish("pizza",[],Bob,[0,0,0,0])
        >>>soup = Dish("soup",[],Lydia,[0,0,0,0])
        >>>sauté = Dish("sauté",[],Joe,[0,0,0,0])
        >>>cake = Dish("Carrot cake",[],Lydia,[0,0,0,0])
        >>>salad = Dish("salad",[],Bob,[0,0,0,0])
        >>>Battle1 = Battle(Lydia,Bob,"tomato",[lasagna,pizza],"")
        >>>Battle2 = Battle(Lydia,Joe,"mushroom",[soup,sauté],"")
        >>>Battle3 = Battle(Joe,Bob,"carrot", [sauté,salad],"")
        >>>kitchen = KitchenStadium([Lydia,Joe],[Bob],INGREDIENTS_LIST,[Battle1,Battle2,Battle3])
        >>>KitchenStadium.get_top_chef(kitchen)
        Joe 
        """
        ratings = {}
        rates = []
        
        for i in self.iron_chefs:
            ratings[(i.record[0])/(i.record[0]+i.record[1]+i.record[2])] = i.name
            rates.append((i.record[0])/(i.record[0]+i.record[1]+i.record[2]))
        
        for i in self.challengers:
            ratings[(i.record[0])/(i.record[0]+i.record[1]+i.record[2])] = i.name
            rates.append((i.record[0])/(i.record[0]+i.record[1]+i.record[2]))
        #I don't know if there is a way to simplify this code 
        rates.sort()
        
        return ratings[rates[-1]]
        
    def get_best_dishes(self):
        """ (KitchenStadium)->Dish
        This functions randomly attributes 4 notes between 1 and 10 to each dish that was prepared in the Kitchen Stadium.
        It returns the dish object that got 4 tens. If there isn't any, it returns None.
        >>>random.seed(11)
        >>>Lydia = Chef("Lydia",(1,2,3),"French")
        >>>Bob = Chef("Bob",(1,2,4), "Japanese")
        >>>lasagna = Dish("lasagna",[],Lydia,[0,0,0,0])
        >>>pizza = Dish("pizza",[],Bob,[0,0,0,0])
        >>>soup = Dish("soup",[],Lydia,[0,0,0,0])
        >>>sauté = Dish("sauté",[],Bob,[0,0,0,0])
        >>>Battle1 = Battle(Lydia,Bob,"tomato",[lasagna,pizza],"")
        >>>Battle2 = Battle(Lydia,Bob,"mushroom",[soup,sauté],"")
        >>>kitchen = KitchenStadium([Lydia],[Bob], INGREDIENTS_LIST,[Battle1,Battle2])
        >>>KitchenStadium.get_best_dishes(kitchen)
        None
        >>>random.seed(12)
        >>>Lydia = Chef("Lydia",(1,2,3),"French")
        >>>Bob = Chef("Bob",(1,2,4), "Japanese")
        >>>lasagna = Dish("lasagna",[],Lydia,[0,0,0,0])
        >>>pizza = Dish("pizza",[],Bob,[0,0,0,0])
        >>>soup = Dish("soup",[],Lydia,[0,0,0,0])
        >>>sauté = Dish("sauté",[],Bob,[0,0,0,0])
        >>>cake = Dish("Carrot cake",[],Lydia,[0,0,0,0])
        >>>salad = Dish("salad",[],Bob,[0,0,0,0])
        >>>Battle1 = Battle(Lydia,Bob,"tomato",[lasagna,pizza],"")
        >>>Battle2 = Battle(Lydia,Bob,"mushroom",[soup,sauté],"")
        >>>Battle3 = Battle(Lydia,Bob,"carrot", [cake,salad],"")
        >>>kitchen = KitchenStadium([Lydia],[Bob],INGREDIENTS_LIST,[Battle1,Battle2,Battle3])
        >>>KitchenStadium.get_best_dishes(kitchen)
        None
        >>>random.seed(16)
        >>>Lydia = Chef("Lydia",(1,2,3),"French")
        >>>Bob = Chef("Bob",(1,2,4), "Japanese")
        >>>lasagna = Dish("lasagna",[],Lydia,[0,0,0,0])
        >>>pizza = Dish("pizza",[],Bob,[0,0,0,0])
        >>>soup = Dish("soup",[],Lydia,[0,0,0,0])
        >>>sauté = Dish("sauté",[],Bob,[0,0,0,0])
        >>>cake = Dish("Carrot cake",[],Lydia,[0,0,0,0])
        >>>salad = Dish("salad",[],Bob,[0,0,0,0])
        >>>Battle1 = Battle(Lydia,Bob,"tomato",[lasagna,pizza],"")
        >>>Battle2 = Battle(Lydia,Bob,"mushroom",[soup,sauté],"")
        >>>Battle3 = Battle(Lydia,Bob,"carrot", [cake,salad],"")
        >>>kitchen = KitchenStadium([Lydia],[Bob],INGREDIENTS_LIST,[Battle1,Battle2,Battle3])
        >>>for i in range(1000):
            KitchenStadium.get_best_dishes(kitchen)
        The output was too long to show but at one point, it did print "sauté"
        """
        ratings = {}
        
        for i in self.battles:
            for j in i.dishes:
                ratings[j.name] = Dish.rate_dish(j)
        
        for i in ratings:
            if ratings[i] == [10,10,10,10]:
                print(i)
        #Difficult to get an output other than None since the probabilities of getting a rating of 10 four times are low
    
    def run_battle(self, iron_chef, challenger):
        """
        """
        
        
        ingredients_list = []
        fobj_i = open("ingredients.txt", "r")
        for line in fobj_i:
            ingredients_list.append(line)
        fobj_i.close()
        
        secret_ingredient = ingredients_list[random.randint(0, 379)]
        
        nouns_list = []
        fobj_n = open("nouns.txt", "r")
        for line in fobj_n:
            nouns_list.append(line)
        fobj_n.close()
        
        names_list = []
        dishes_ingredients = []
        for i in range(4):
            names_list.append(nouns_list[random.randint(0, 499)] + secret_ingredient)
            dish_ingredients = [secret_ingredient]
            for i in range(3):
                dish_ingredients.append(ingredients_list[random.randint(0, 379)])
            dishes_ingredients.append(dish_ingredients)
        
#is it same 2 dish for the 2 contestant?      

        #Creating 4 dishes
        dish1 = Dish(names_list[0], dishes_ingredients[0], iron_chef)
        dish2 = Dish(names_list[1], dishes_ingredients[1], iron_chef)
        dish3 = Dish(names_list[2], dishes_ingredients[2], challenger)
        dish4 = Dish(names_list[3], dishes_ingredients[3], challenger)
    
        dishes = [dish1, dish2, dish3, dish4]  
        
        #Creating the battle
        battle_iron_vs_chal = Battle(iron_chef, challenger, secret_ingredient, dishes, outcome="")
        
        #Adding the battle to the list of battles
        battles.append(battle_iron_vs_chal)
        
        #Concluding battle, updating chefs' record
        if battle_iron_vs_chal.conclude() == "iron_chef":
            record_list = list(iron_chef.record)
            record_list[0] += 1
            iron_chef.record = tuple(record_list)
            
            record_list = list(challenger.record)
            record_list[1] += 1
            challenger.record = tuple(record_list)
            
        elif battle_iron_vs_chal.conclude() == "challenger":
            record_list = list(iron_chef.record)
            record_list[1] += 1
            iron_chef.record = tuple(record_list)
            
            record_list = list(challenger.record)
            record_list[0] += 1
            challenger.record = tuple(record_list)
            
        else:
            record_list = list(iron_chef.record)
            record_list[2] += 1
            iron_chef.record = tuple(record_list)
            
            record_list = list(challenger.record)
            record_list[2] += 1
            challenger.record = tuple(record_list)
        
        
        
        
        
        
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




