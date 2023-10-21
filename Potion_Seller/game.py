from __future__ import annotations
from avl import AVLTree
# ^ In case you aren't on Python 3.10

from hash_table import LinearProbePotionTable

from random_gen import RandomGen
from potion import Potion
from avl import AVLTree
from array_list import ArrayList

class Game:
    """
    Class to play the game
    """
    
    def __init__(self, seed=0) -> None:
        """
        Initialization for Game class
        Contains a RandomGen object to generate a random integer later
        C is the total number of potion in inventory currently in stock
        save is used to save the potion inventory, so we can return it after choosing potion for vendor
        vendor is used to save the potion data
        """
        self.rand = RandomGen(seed=seed)
        self.C = 0
        self.save = []
        self.vendor = []

    
    def set_total_potion_data(self, potion_data: list) -> None:
        """
        Method to save all the possible potions.
        Data Structure that is used is hash table to have O(1) insert and access.
        Function will save the potion data to vendor to use in later function
        Hash table size is chosen based on the amount of potion given
        For every potion given in potion_data, it will create a Potion object and input it in the hash table
        Best Time Complexity is O(1) when inserting, the first spot is empty
        Average Time Complexity is O(C), C for the amount of potion in potion_data. 
        Worst Time Complexity is O(C * n) where C is the len of potion data, and n is the hash table size.
        The worst time complexity is very unlikely to happen because of how hash table works. The hash function will make the key unique for most items.
        """
        # Save the list into the attribute self.vendor that will be used for solve_game later
        self.vendor = potion_data

        # Create the hash table
        max_potions = len(potion_data)
        self.hashtable = LinearProbePotionTable(max_potions)
        # Set the inventory of the vendors to contain 0 Litres of every potion listed
        for i in range(len(potion_data)):
            potion_data[i] = Potion.create_empty(potion_data[i][0], potion_data[i][1], potion_data[i][2])
            # Insert these potions into the hash table
            self.hashtable.insert(potion_data[i].get_name(), potion_data[i])

    def add_potions_to_inventory(self, potion_name_amount_pairs: list[tuple[str, float]]) -> None:
        """
        Method to add potions from the list of potions to the inventory
        Data Structure used for the inventory is an AVL Tree for O(log n) insertion
        The method will save the potions available in the inventory into the save variable to readd later after vendor chooses potions
        The method will check if the potion given is in the hash table, and sets the quantity of the potion to the amount given in the argument
        Next, it will put the potions into the AVLTree with the buy price as the key and Potion object as the value
        Lastly, it will set the C to the amount of potion given to use later
        Time Complexity is O(C * log n) where C is the amount of potion given (len(potion_name_amount_pairs)) and log n is the insertion into the AVLTree
        """
        # save the "potion_name_amount_pairs" to reset inventory later
        self.save = potion_name_amount_pairs

        # Create the avl tree
        self.tree = AVLTree()
        # Add the potions with quantity > 0 into the avl tree
        for item in potion_name_amount_pairs:
            if item[0] in self.hashtable:
                # set the quantity given from "potion_name_amount_pairs" for each potion in the hash table
                self.hashtable[item[0]].set_quantity(item[1])
                # insert the potion into the avl tree according to the key "buy_price" of the potion
                self.tree[self.hashtable[item[0]].get_buy_price()] = self.hashtable[item[0]]

        # save the total number of potions which are currently in stock (len(potion_name_amount_pairs)) to the attribute self.C
        # needed to pick a random number from 1 to C (inclusive) later
        self.C = len(potion_name_amount_pairs)
                

    def choose_potions_for_vendors(self, num_vendors: int) -> list:
        """
        Method to choose the potions for the vendors
        It will output a list containing tuples, each tuple containing the name and quantity of the potion
        It uses the RandomGen class to generate random number which will be used to take the kth largest potion in the inventory
        It will take the kth most expensive item in the inventory, and add it to vendor_list
        It will also delete the potion from the AVLTree inventory, as to avoid vendors taking the same potion
        The function will call add_potions_to_inventory with the saved list from before
        kth_largest function used is O(log n), add_potions_to_inventory is O(C * log n), ArrayList append is O(1), delete from tree is O(log n)
        So, the Time Complexity is O(C * log n) where C is the num_vendors given and n is the number of potion provided previously
        """

        # vendor list used to show the potions that the vendors are selling
        vendor_list = ArrayList(num_vendors)
        rgen = RandomGen()

        # Process of picking a potion:
        # Select a random number "P" from 1 to C (inclusive)
        # The vendor will pick the "Pth" most expensive potion from the inventory
        # Add this potion to the list
        # remove the potion from the avl tree
        # decrement self.C by 1
        # repeat the process
        for num in range(num_vendors): # add items to vendor list according to the number of vendors
            val = rgen.randint(self.C)
            most_expensive = self.tree.kth_largest(val)
            most_expensive_potion_type = most_expensive.item.get_name()
            selling_item = self.hashtable[most_expensive_potion_type]
            vendor_list.append((str(selling_item.get_name()), int(selling_item.get_quantity())))
            del self.tree[most_expensive.key]
            self.C -= 1

        # At the end of the process, all vendors add the potions back into inventory.
        self.add_potions_to_inventory(self.save)
        
        return vendor_list

    def solve_game(self, potion_valuations: list[tuple[str, float]], starting_money: list[int]) -> list[float]:
        """
        The method will solve the game with two input argument
        potion_valuations contains list of tuples with the name of the potion and the selling price to the adventurer
        starting_money will contain list of floats, which is the starting money for each day
        The first step of the function is to prepare the ArrayList:
        1. Take Potion object, sell price to adventurer (potion_valuations), and profit (buy price from vendor - sell price to adventurer)
        2. Put the three elements inside a tuple and append it to the ArrayList
        3. Using Merge Sort, sort the ArrayList according to greatest profit and least buy price
        
        Then, we will do days according to the length of starting money.
        For each day, it will do the following:
        1. Take the Potion object stored in index 0 of the tuples inside sorted_array
        2. Count how many potion we can buy by dividing our money by the buy_price from vendor
        3. Check if the amount that we can buy exceeds the quantity of the potion, if yes, change the amount we buy to the amount of that potion
        4. Else, we count how much money we earn by multiplying the amount that we buy by the sell_price to adventurer (index 1 of the tuples inside sorted_array)
        5. Decrease our money by how much we spent by multiplying the amount that we buy to the buy_price from vendor
        6. Append the total money we earned during the day to result list
        7. Repeat for each day (money in starting_money)
        8. Return the result list
        Because there are merge sort (n log n )and we can play it for multiple days (M*N)
        Time Complexity is O(n log n + M * N)
        """
        sorted_array = ArrayList(len(potion_valuations))

        for item in potion_valuations:
            potion_data = self.hashtable[item[0]] #Take potion object from the hashtable
            buy_price_vendor = potion_data.get_buy_price() #Get the buy price from the vendor
            sell_price_adventurer = item[1] #The sell price to the adventurer
            profit_total = sell_price_adventurer - buy_price_vendor #The profit that we get
            
            sorted_array.append((potion_data, sell_price_adventurer, profit_total)) #Input tuple of potion_data, selling price, and profit of each potion
            
        #Complexity = O(n log n)
        self.merge_sort(sorted_array) # Merge sort according to its profit
        # for i in sorted_array:
        #     print("Buy Price " + str(i[0].get_buy_price()))
        #     print("Profit " + str(i[2]))

        result = [] 
        for money in starting_money:
            current_money = money
            total_profit = 0 #Total profit earned during the day
            i = 0 #Indexing
            while current_money > 0:
                most_profit_potion = sorted_array[i] #Get the tuple from sorted_array
                potion_object = most_profit_potion[0] #Take potion object
                potion_count = current_money / potion_object.get_buy_price() #Amount of potion to buy

                if potion_count > potion_object.get_quantity(): #Check if the amount to buy exceeds potion quantity
                    potion_count = potion_object.get_quantity()  #If yes, set the potion to buy to the quantity
                
                total_profit += potion_count * most_profit_potion[1] #Count how much money we earn
                current_money -= potion_count * potion_object.get_buy_price() #Subtract our money by our buying price
                i += 1 #Decrease the i to go to the next most profitable potion
            result.append(total_profit) #Append to the final result
        return result
    
    def merge_sort(self, array):
        """
        Merge Sort modified to work with a tuple (potion_data, sell_price_adventurer, profit_total)
        The function will sort by the greatest profit and least buy price of each potion
        Time Complexity is O(n log n)
        """
        if len(array) > 1:

            mid = len(array)//2
            left = array[:mid]
            right = array[mid:]

            #Sort left and right half
            self.merge_sort(left)
            self.merge_sort(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                #MODIFIED CONDITION
                #Index 2 is profit, this is where it sorts according to the profit
                #Second Condition is to check, if the profit is the same, then we will sort it according to a lower buy price
                #So, the final list elements will be the greatest profit and lowest buy price to least profit and highest buy price
                if left[i][2] > right[j][2] or (left[i][2] == right[j][2] and left[i][0].get_buy_price()<right[j][0].get_buy_price()):
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
           

# g = Game()
# g.set_total_potion_data([
#     (str(x), str(x), x)
#     for x in range(1, 101)
# ])

# g.add_potions_to_inventory([
#     (str(x), x)
#     for x in range(2, 101)
# ])

# print(g.choose_potions_for_vendors(14))

# print(g.choose_potions_for_vendors(99))

# print(len(res2) == 99)



# G = Game()

# G.set_total_potion_data([
#     # Category, Name, Buying price from vendors.
#     ["Health", "Potion of Health Regeneration", 20],
#     ["Buff", "Potion of Extreme Speed", 10],
#     ["Damage", "Potion of Deadly Poison", 45],
#     ["Health", "Potion of Instant Health", 5],
#     ["Buff", "Potion of Increased Stamina", 25],
#     ["Damage", "Potion of Untenable Odour", 1],
# ])

# # Start of Day 1
# # Let’s begin by adding to the inventory of PotionCorp:
# G.add_potions_to_inventory([
#     ("Potion of Health Regeneration", 4),
#     ("Potion of Extreme Speed", 5),
#     ("Potion of Instant Health", 3),
#     ("Potion of Increased Stamina", 10),
#     ("Potion of Untenable Odour", 5),
# ])

# full_vendor_info = [
#     ("Potion of Health Regeneration", 30),
#     ("Potion of Extreme Speed", 15),
#     ("Potion of Instant Health", 15),
#     ("Potion of Increased Stamina", 20),
# ]

# # Play the game with 3 attempts, at different starting money.
# results = G.solve_game(full_vendor_info, [12.5, 45, 80])
# print(results)


# DIFFERENCE

# G = Game()
# # There are these potions, with these stats, available over the course of the game.
# G.set_total_potion_data([
#     # Name, Category, Buying price from vendors.
#     ["Potion of Health Regeneration", "Health", 20],
#     ["Potion of Extreme Speed", "Buff", 10],
#     ["Potion of Deadly Poison", "Damage", 45],
#     ["Potion of Instant Health", "Health", 5],
#     ["Potion of Increased Stamina", "Buff", 25],
#     ["Potion of Untenable Odour", "Damage", 1],
# ])

# # Start of Day 1
# # Let’s begin by adding to the inventory of PotionCorp:
# G.add_potions_to_inventory([
#     ("Potion of Health Regeneration", 4),
#     ("Potion of Extreme Speed", 5),
#     ("Potion of Instant Health", 3),
#     ("Potion of Increased Stamina", 10),
#     ("Potion of Untenable Odour", 5),
# ])

# full_vendor_info = [
#     ("Potion of Health Regeneration", 30),
#     ("Potion of Extreme Speed", 15),
#     ("Potion of Instant Health", 15),
#     ("Potion of Increased Stamina", 20),
# ]

# # Play the game with 3 attempts, at different starting money.
# results = G.solve_game(full_vendor_info, [12.5, 45, 80])
