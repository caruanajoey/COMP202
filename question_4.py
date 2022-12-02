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
        
        return "Name: " + self.name + "\n\tWins: "+ str(wins) + "\n\tLosses: " + str(losses) + "\n\tTies: "+ str(ties) + "\n\tCuisine: "+ self.cuisine
        
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
        
        temp_string = ""
        for i in self.ingredients:
            temp_string += (i+", ")
        
        return "Chef: " + self.chef.name + "\n\tDish: " + self.name + "\n\tIngredients: " + temp_string[:-2] + "\n\tRatings: " + str(self.ratings)

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
        
        temp_string = ""
        for i in self.dishes:
            temp_string += ("\n" + str(i))
        
        return "Iron Chef: " + self.iron_chef.name + "\nChallenger: " + self.challenger.name + "\nSecret ingredient: " + self.secret_ingredient + "\n--Dishes-- " + temp_string + "\nOutcome: " + self.outcome

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
    def __init__(self, iron_chefs, challengers, ingredients, battles=[]):
        
        self.iron_chefs = iron_chefs
        self.challengers = challengers
        self.ingredients = ingredients
        self.battles = battles
        
    def __str__(self):
        
        temp_string1 = ""
        temp_string2 = ""
        temp_string3 = ""
        
        for i in self.iron_chefs:
            temp_string1 += (str(i) + "\n")
        for i in self.challengers:
            temp_string2 += (str(i) + "\n")
        for i in range(len(self.battles)):
            temp_string3 += ("\nRound #" + str(i+1) + ":\n" + (str(self.battles[i])) + "\n")
        
        return "---Chef Info ---\n\n--Iron Chefs--\n" + temp_string1 + "--Challengers--\n" + temp_string2 + "\n----Battles----\n" + temp_string3

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
            
            if i.record[0]+i.record[1]+i.record[2] != 0:
                ratings[(i.record[0])/(i.record[0]+i.record[1]+i.record[2])] = i.name
                rates.append((i.record[0])/(i.record[0]+i.record[1]+i.record[2]))
            else:
                continue
        
        for i in self.challengers:
            
            if i.record[0]+i.record[1]+i.record[2] != 0:
                ratings[(i.record[0])/(i.record[0]+i.record[1]+i.record[2])] = i.name
                rates.append((i.record[0])/(i.record[0]+i.record[1]+i.record[2]))
            else:
                continue
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
                ratings[j.name] = j.ratings
        
        for i in ratings:
            if ratings[i] == [10,10,10,10]:
                return i
            
        #Difficult to get an output other than None since the probabilities of getting a rating of 10 four times are low
    
    def run_battle(self, iron_chef, challenger):
        """
        """
        
        ingredients_list = self.ingredients
        
        secret_ingredient = ingredients_list[random.randint(0, 379)]
        
        nouns_list = NOUNS_LIST
        
        names_list = []
        dishes_ingredients = []
        for i in range(4):
            names_list.append(nouns_list[random.randint(0, 499)] + secret_ingredient)
            dish_ingredients = [secret_ingredient]
            dishes_number = random.randint(1,3) #Randomly chooses whether dish will have 1, 2, or 3 additional ingredients
            for i in range(dishes_number):
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
        self.battles.append(battle_iron_vs_chal)
        
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


### Game Engine ###

classlist = ['Alina Lu', 'Audrey-Anne Beaudry', 'Domenic Continelli', 'Emile Vienneau', 'Eva Koall', 'Giuseppe Caruana', 'Isabelle Ho', 'Isbat-ul Islam', 'Jeffrey Kauv Li', 'Jerry Gao', 'Laura Waters', 'Laurence Perreault', 'Marlo Anzarut', 'Natasha Bejjani', 'Patrick Wilson', 'Philippe Aprahamian', 'Rachel Shi', 'Sophie Courville', 'Visali Kandiah', 'Zachary Quirion-Haddine']
cuisines = ['Mexican Cuisine', 'Japanese Cuisine', 'Cambodian Cuisine', 'Italian Cuisine', 'Argentinian Cuisine', 'Ethiopian Food', 'Canadian Food', 'Guatemalan Cuisine', 'Taiwanese Cuisine', 'Seafood', 'Israeli Cuisine', 'Brazilian Food', 'Turkish Cuisine', 'Pakistani Cuisine', 'United Kingdom Cuisine', 'Portuguese Food', 'Vietnamese Food', 'South African Cuisine', 'Chilean Cuisine', 'Hawaiian Food', 'Russian Food']
challengers = []
for i in range(len(classlist)):
    challengers.append(Chef(classlist[i], (0, 0, 0), cuisines[random.randint(0, len(cuisines)-1)]))

teachers = ['Hamza Javed', 'Jonathan Campbell']
iron_chefs = []
for i in range(len(teachers)):
    iron_chefs.append(Chef(teachers[i], (0, 0, 0), cuisines[random.randint(0, len(cuisines)-1)]))



group_11_battle = KitchenStadium(iron_chefs, challengers, INGREDIENTS_LIST)

command = ""
while command != "end":
    iron_chef = group_11_battle.iron_chefs[random.randint(0, len(group_11_battle.iron_chefs)-1)]
    challenger = group_11_battle.challengers[random.randint(0, len(group_11_battle.challengers)-1)]
    if command == "best dishes":
        print("Best dishes: " + str(group_11_battle.get_best_dishes()) + "\n")
    elif command == "top chef":
        print("Top chef: " + group_11_battle.get_top_chef() + "\n")
    elif command == "chef info":
        temp_string1 = ""
        temp_string2 = ""
        
        for i in group_11_battle.iron_chefs:
            temp_string1 += (str(i) + "\n")
        for i in group_11_battle.challengers:
            temp_string2 += (str(i) + "\n")
        
        print("---Chef Info---\n\n--Iron Chefs--\n" + temp_string1 + "--Challengers--\n" + temp_string2)
    elif command == "":
        group_11_battle.run_battle(iron_chef, challenger)
        print(group_11_battle)
    else:
        print("Invalid command; Commands: \'best dishes\', \'top chef\', \'chef info\', or press Enter to continue battles.")
    command = input("Command: ")
    print("\n")



