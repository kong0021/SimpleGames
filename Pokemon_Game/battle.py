from poke_team import PokeTeam
from queue_adt import CircularQueue
from stack_adt import ArrayStack
from array_sorted_list import ArraySortedList
from sorted_list import ListItem
from pokemon import Charmander, Bulbasaur, Squirtle, MissingNo

class Battle:
    def __init__(self, trainer_one_name: str, trainer_two_name: str):
        # Create objects separately for team1 and team2, and set the initial battle_mode to None
        self.team1 = PokeTeam(trainer_one_name)
        self.team2 = PokeTeam(trainer_two_name)
        self.battle_mode = None

    def fight(self, pokemon1, pokemon2):
        """
        Overall time complexity = O(1):
        What this method consists of:
        1. getter and setter methods - time complexity of O(1)
        2. comparison operations - time complexity of O(1)
        3. calculate_attacked_damage() performs basic operations - time complexity of O(1)

        Best time complexity = O(1),
        Worst time complexity = O(1), Since Overall time complexity = O(1), Best time complexity = Worst time complexity

        This method is used to allow two pokemons to fight each other and change their current HP and level after fighting
        The method will return the winner of the two fighters

        """

        # Calculate damage and set_hp
        if pokemon1.get_speed() > pokemon2.get_speed():  # If P1's speed is greater than P2, P1 attacks and P2 defends
            pokemon2.calculate_attacked_damage(pokemon1)
            if pokemon2.get_HP() > 0: # If P2 is still alive, P2 now attacks
                pokemon1.calculate_attacked_damage(pokemon2)
        elif pokemon2.get_speed() > pokemon1.get_speed():  # If P2's speed is greater than P1, P2 attacks and P1 defends
            pokemon1.calculate_attacked_damage(pokemon2)
            if pokemon1.get_HP() > 0: # If P1 is still alive, P1 now attacks
                pokemon2.calculate_attacked_damage(pokemon1)
        elif pokemon2.get_speed() == pokemon1.get_speed():  # If P1's and P2's speed are identical, both attack and defend simultaneously
            pokemon1.calculate_attacked_damage(pokemon2)
            pokemon2.calculate_attacked_damage(pokemon1)

        # If both P1's and P2's health is <= 0, no one won the fight, therefore return None
        if pokemon1.get_HP() <= 0 and pokemon2.get_HP() <= 0:
            return None

        # If both P1's and P2's health is > 0, both pokemons will lose 1 hp
        elif pokemon1.get_HP() > 0 and pokemon2.get_HP() > 0:
            pokemon1.set_HP(pokemon1.get_HP() - 1)
            pokemon2.set_HP(pokemon2.get_HP() - 1)

            # Check if P2 is still alive and P1 has fainted after losing 1 HP
            # If P2 is still alive, increase its level by 1
            if pokemon1.get_HP() <= 0 and pokemon2.get_HP() > 0:
                pokemon2.set_level(pokemon2.get_level() + 1)   # Increase P2 level by 1 after defeating P1
                return pokemon2.get_name() # Return the winner's name which is P2

            # Check if P1 is still alive and P2 has fainted after losing 1 HP
            # If P1 is still alive, increase its level by 1
            elif pokemon2.get_HP() <= 0 and pokemon1.get_HP() > 0:
                pokemon1.set_level(pokemon1.get_level() + 1) # Increase P1 level by 1 after defeating P2
                return pokemon1.get_name() # Return the winner's name which is P1
            else:
                # If both pokemons are still alive after losing 1 hp
                # return both P1'S and P2'S name
                return pokemon1.get_name(), pokemon2.get_name()

        # Check if P2 is still alive and P1 has fainted after fighting, if P2 is still alive increase its level by 1
        elif pokemon1.get_HP() <= 0 and pokemon2.get_HP() > 0:
            pokemon2.set_level(pokemon2.get_level() + 1) # Increase P2 level by 1 after defeating P1
            return pokemon2.get_name() # Return the winner's name which is P2

        # Check if P1 is still alive and P2 has fainted after fighting, if P1 is still alive increase its level by 1
        elif pokemon2.get_HP() <= 0 and pokemon1.get_HP() > 0:
            pokemon1.set_level(pokemon1.get_level() + 1) # Increase P1 level by 1 after defeating P2
            return pokemon1.get_name() # Return the winner's name which is P1

    def rotate(self, team_array):
        """
        Overall time complexity = O(1)
        What this method consists of:
        1. accessing array[i] - time complexity of O(1)
        2. performing queue.serve() - time complexity of O(1)
        3. performing queue.append() - time complexity of O(1)


        Best time complexity = O(1)
        Worst time complexity = O(1), Since Overall time complexity = O(1), Best time complexity = Worst time complexity

        This method is used to rotate the pokemon at the start of the queue, and move it to the back of the queue
        """

        # If array length == 1, there is no need to rotate the pokemon and set a new pokemon
        # else, perform rotation
        if team_array.length == 1:
            pass
        else:
            save = team_array.array[team_array.front] # Save the first pokemon at the start of the queue
                                                      # as it will be added to the back of the queue later
            team_array.serve() # remove the first item at the start of the queue
            team_array.append(save) # append the saved pokemon to the back of the queue

        return team_array # Return the new team_array

    def poketype_sort(self, team_array): # O(N)
        """
        The function poketype_sort loops the array sorted list passed in as the parameter with i as the counter.
        It has the condition while i is less than the index of the last ListItem in the array, check if the key
        attribute of ListItem object at i is same as the key of ListItem object at i+1, if it is, check whether the
        ListItem object at i is equal to Charmander, if the ListItem objects at both indexes have "Charmander"
        increment i and continue the loop, if not, swap the at objects at index i and i+1 and set the counter to
        zero to check if it is sorted. The same is done for Bulbasaur objects, if ListItem at index i is Bulbasaur,
        check if the ListItem object at the next index is Charmander or Bulbasaur, if condition is fulfilled, the
        counter is incremented and the loop continues, if not, swap the objects at i with i+1 and set counter to
        zero to check again. This should sort the list in the order of priority as Charmander->Bulbasaur->Squirtle.
        The best and worst case time complexity of this function is O(n) as there are no properties of elements
        that reduce big O.
        """
        # Charmanders -> Bulbasaurs -> Squirtles
        i = 0
        while i < len(team_array) - 1:

            if team_array.array[i].key == team_array.array[i + 1].key:
                if team_array.array[i].value.get_name() == "Charmander":
                    if team_array.array[i].value.get_name() == team_array.array[i + 1].value.get_name():
                        i += 1
                    else:

                        team_array.array[i], team_array.array[i + 1] = team_array.array[i + 1], team_array[i]
                        i = 0
                elif team_array.array[i].value.get_name() == "Bulbasaur":
                    if team_array.array[i + 1].value.get_name() == "Charmander" or team_array.array[
                        i].value.get_name() == team_array.array[i + 1].value.get_name():
                        i += 1
                    else:

                        team_array.array[i], team_array.array[i + 1] = team_array.array[i + 1], team_array.array[i]
                        i = 0
                else:
                    i += 1
            else:
                i += 1
        return team_array

    def set_mode_battle(self):
        """
        Overall time complexity = O(N)
        What this method consists of:
        1. While loop - Best: O(1) if the first user input is correct, Worst: O(N) if the first user input is not correct
        2. choose_team() method - Best: O(1) if the first user input is correct, Worst: O(N) if the first user input is not correct
        3. assign_team() method - time complexity of O(N), contains a for loop
        4. stack.push() method - time complexity of O(1)
        5. stack.pop() method - time complexity of O(1)

        Best time complexity = O(N)
        Worst time complexity = O(N)

        This method is used to let two teams fight each other until one or both of the team's pokemons have all fainted
        and a pokemon will be removed from his/her team after fainting
        """


        # First set mode battle to 0 and create the stack for team 1
        print("Team 1:")
        stack = self.team1.choose_team(0, None) # Best = O(N), Worst = O(N)

        # Check if the user has inputted a fourth value/MissingNo for team 1
        total = stack[0] + stack[1] + stack[2] # stack[0] = charm, stack[1] = bulb, stack[2] = squir
        if stack[3] == True and total < 6:
            glitch1 = True # If a fourth value is found, Then there's a glitch for team 1
        else:
            glitch1 = False # If a fourth value is not found, then there's no glitch for team 1

        # Create the team by placing the pokemons into the stack/team 1
        team_array_1 = self.team1.assign_team(stack[0], stack[1], stack[2]) # Best = O(N), Worst = O(N)

        # First set mode battle to 0 and create the stack for team 2
        print("Team 2:")
        stack = self.team2.choose_team(0, None) # Best = O(N), Worst = O(N)

        # Check if the user has inputted a fourth value/MissingNo for team 2
        total = stack[0] + stack[1] + stack[2] # stack[0] = charm, stack[1] = bulb, stack[2] = squir
        if stack[3] == True and total < 6:
            glitch2 = True # If a fourth value is found, Then there's a glitch for team 2
        else:
            glitch2 = False # If a fourth value is not found, then there's no glitch for team 2

        # Create the team by placing the pokemons into the stack/team 2
        team_array_2 = self.team2.assign_team(stack[0], stack[1], stack[2]) # Best = O(N), Worst = O(N)

        # Assign pokemon1 to fight for team 1 and pokemon2 to fight for team2
        # Where pokemon1 and pokemon2 are found at the end of the stack
        pokemon1 = team_array_1.array[team_array_1.length - 1] # O(1)
        pokemon2 = team_array_2.array[team_array_2.length - 1] # O(1)

        # The reason why this code is here is explained later
        glitched1 = False
        glitched2 = False

        # Now let the two teams fight until one or both teams are empty
        while not team_array_1.is_empty() and not team_array_2.is_empty(): # Best: O(1), Worst: O(N)

            # Calculate damage and set_hp for the pokemons that are fighting
            self.fight(pokemon1, pokemon2) # O(1)

            # If both P1's and P2's health is <= 0, remove both from stack
            if pokemon1.get_HP() <= 0 and pokemon2.get_HP() <= 0:
                print("team 1's " + str(
                    team_array_1.array[team_array_1.length - 1].NAME) + " and team 2's " + str(
                    team_array_2.array[team_array_2.length - 1].NAME) + " both faint ")

                # P1 and P2 are at the end of the stack
                # By using the method pop() we will remove these two pokemons from the stack
                team_array_1.pop() # O(1)
                team_array_2.pop() # O(1)
                # Now assign the next fighters P1 and P2, which are at the end of the stack
                pokemon1 = team_array_1.array[team_array_1.length - 1] # O(1)
                pokemon2 = team_array_2.array[team_array_2.length - 1] # O(1)

            # If P1's health is <= 0, remove P1 from the stack
            elif pokemon1.get_HP() <= 0:
                print("team 1's " + str(
                    team_array_1.array[team_array_1.length - 1].NAME) + " gets fainted by team 2's " + str(
                    team_array_2.array[team_array_2.length - 1].NAME))
                team_array_1.pop() # O(1), remove P1 found at the end of the stack
                # Assign the next fighter P1, which is at the end of the stack
                pokemon1 = team_array_1.array[team_array_1.length - 1] # O(1)

            # If P2's health is <= 0, remove P2 from the stack
            elif pokemon2.get_HP() <= 0:
                print("team 1's " + str(team_array_1.array[team_array_1.length - 1].NAME) + " faints team 2's " + str(
                    team_array_2.array[team_array_2.length - 1].NAME))
                team_array_2.pop() # O(1), remove P2 found at the end of the stack
                # Assign the next fighter P2, which is at the end of the stack
                pokemon2 = team_array_2.array[team_array_2.length - 1] # O(1)

            # If team array 1 is empty and glitch1 is true
            # This means that there is a MissingNo object left to fight for team 1
            # Therefore, create another stack of size 1 as the max MissingNo objects available
            # to fight for a team is 1. Then place this MissingNo object into the stack and let it fight
            # This same rule applies for team 2

            # This code only needs to run once after adding MissingNo to the stack/team,
            # Which is why we set glitched1 and glitched2 to True after
            # This same rule applies for team 2

            if team_array_1.is_empty() and glitch1 and glitched1 == False:
                self.stack = ArrayStack(1) # Create stack of size 1
                pokemon1 = MissingNo() # Create MissingNo() object named pokemon1
                self.stack.push(pokemon1) # O(1), Add pokemon1 to the stack
                team_array_1 = self.stack # Name the stack as team1_array
                glitched1 = True
            if team_array_2.is_empty() and glitch2 and glitched2 == False:
                self.stack = ArrayStack(1) # Create stack of size 1
                pokemon2 = MissingNo() # Create MissingNo() object named pokemon2
                self.stack.push(pokemon2) # O(1), Add pokemon2 to the stack
                team_array_2 = self.stack # Name the stack as team2_array
                glitched2 = True

        # Announce the winner or draw
        if team_array_1.is_empty() and team_array_2.is_empty(): # O(1), If both teams are empty, It's a draw
            print("It's a draw")
            return "It's a draw"
        elif team_array_1.is_empty(): # If team 1 is empty, return team 2's name which is the winner
            print(self.team2.trainer_name)
            return self.team2.trainer_name
        elif team_array_2.is_empty(): # If team 2 is empty, return team 1's name which is the winner
            print(self.team1.trainer_name)
            return self.team1.trainer_name

    def rotating_mode_battle(self) -> str:
        """
        Overall time complexity = O(N)
        What this method consists of:
        1. choose_team() method - Best: O(1) if the first user input is correct, Worst: O(N) if the first user input is not correct
        2. assign_team() method - time complexity of O(N), contains a for loop
        3. queue.append() - time complexity of O(1)
        4. queue.serve() - time complexity of O(1)

        Best time complexity = O(N)
        Worst time complexity = O(N)

        This method is used to let two teams fight each other until one or both team's pokemons have fainted
        and a pokemon will rotate to the back of his/her team after fainting his/her opponent
        """


        # First set mode battle to 1 and create the queue for team 1
        queue = self.team1.choose_team(1, None) # Best = O(N), Worst = O(N)

        # Check if the user has inputted a fourth value/MissingNo for team 1
        total = queue[0] + queue[1] + queue[2]  # queue[0] = charm, queue[1] = bulb, queue[2] = squir
        if queue[3] == True and total < 6:
            glitch1 = True # If a fourth value is found, Then there's a glitch for team 1
        else:
            glitch1 = False # If a fourth value is not found, then there's no glitch for team 1

        # Create the team by placing the pokemons into the stack/team 1
        team_array_1 = self.team1.assign_team(queue[0], queue[1], queue[2]) # O(N)

        # First set mode battle to 1 and create the queue for team 2
        queue = self.team2.choose_team(1, None) # Best = O(N), Worst = O(N)

        # Check if the user has inputted a fourth value/MissingNo for team 2
        total = queue[0] + queue[1] + queue[2]  # queue[0] = charm, queue[1] = bulb, queue[2] = squir
        if queue[3] == True and total < 6:
            glitch2 = True # If a fourth value is found, Then there's a glitch for team 2
        else:
            glitch2 = False # If a fourth value is not found, then there's no glitch for team 2

        # Create the team by placing the pokemons into the stack/team 2
        team_array_2 = self.team2.assign_team(queue[0], queue[1], queue[2]) # O(N)

        # Assign pokemon1 to fight for team 1 and pokemon2 to fight for team 2
        # Where pokemon1 and pokemon2 are found at the front of the queue
        self.pokemon1 = team_array_1.array[team_array_1.front]
        self.pokemon2 = team_array_2.array[team_array_2.front]

        # The reason why this code is here is explained later
        glitched1 = False
        glitched2 = False

        # Now let the two teams fight until one or both teams are empty
        while not team_array_1.is_empty() and not team_array_2.is_empty(): # O(N)

            # Calculate damage and set_hp for the pokemons that are fighting
            self.fight(self.pokemon1, self.pokemon2) # O(1)

            # If both pokemon's health are > 0 after fighting
            # If it is, rotate both to the back of the stack
            if self.pokemon1.get_HP() > 0 and self.pokemon2.get_HP() > 0:
                print("Both team 1's " + str(team_array_1.array[team_array_1.front].NAME) + " and team 2's " + str(
                    team_array_2.array[team_array_2.front].NAME) + " live")
                print("team 1's " + str(self.pokemon1.NAME) + " HP is " + str(self.pokemon1.get_HP()) + " and team 2's " + str(self.pokemon2.NAME) + " HP is " + str(self.pokemon2.get_HP()))
                print("\n")

                # Rotate pokemon1 to the back in team 1
                self.rotate(team_array_1) # Best and worst time complexity = O(1)

                # Set new pokemon fighter for team 1, found at the front of the queue
                self.pokemon1 = team_array_1.array[team_array_1.front]

                # Rotate pokemon2 to the back in team 2
                self.rotate(team_array_2) # Best and worst time complexity = O(1)

                # Set new pokemon fighter for team 2, found at the front of the queue
                self.pokemon2 = team_array_2.array[team_array_2.front]

            # If both P1's and P2's health is <= 0, remove both from queue
            elif self.pokemon1.get_HP() <= 0 and self.pokemon2.get_HP() <= 0:
                print("team 1's " + str(
                    team_array_1.array[team_array_1.front].NAME) + " and team 2's " + str(
                    team_array_2.array[team_array_2.front].NAME) + " both faint")
                print("team 1's " + str(self.pokemon1.NAME) + " HP is " + str(self.pokemon1.get_HP()) + " and team 2's " + str(self.pokemon2.NAME) + " HP is " + str(self.pokemon2.get_HP()))
                print("\n")

                # Remove pokemon1 and pokemon2 at the start of the queue
                team_array_1.serve() # O(1)
                team_array_2.serve() # O(1)
                # Set new pokemon fighters for team 1 and team 2, found at the front of the queue
                self.pokemon1 = team_array_1.array[team_array_1.front]
                self.pokemon2 = team_array_2.array[team_array_2.front]

            # If P1's health is <= 0, remove P1 from the stack
            elif self.pokemon1.get_HP() <= 0:
                print("team 1's " + str(
                    team_array_1.array[team_array_1.front].NAME) + " gets fainted by team 2's " + str(
                    team_array_2.array[team_array_2.front].NAME))
                print("team 1's " + str(self.pokemon1.NAME) + " HP is " + str(self.pokemon1.get_HP()) + " and team 2's " + str(self.pokemon2.NAME) + " HP is " + str(self.pokemon2.get_HP()))
                print("\n")

                # Remove pokemon1 at the start of the queue
                team_array_1.serve() # O(1)

                # Set new pokemon fighter for team 1, found at the front of the queue
                self.pokemon1 = team_array_1.array[team_array_1.front]

                # Rotate pokemon2 to the back in team 2 after defeating P1
                self.rotate(team_array_2) # O(1)

                # Set new pokemon fighter for team 2, found at the front of the queue
                self.pokemon2 = team_array_2.array[team_array_2.front]

            # If P2's health is <= 0, remove P2 from the stack
            elif self.pokemon2.get_HP() <= 0:
                print("team 1's " + str(team_array_1.array[team_array_1.front].NAME) + " faints team 2's " + str(
                    team_array_2.array[team_array_2.front].NAME))
                print("team 1's " + str(self.pokemon1.NAME) + " HP is " + str(self.pokemon1.get_HP()) + " and team 2's " + str(self.pokemon2.NAME) + " HP is " + str(self.pokemon2.get_HP()))
                print("\n")

                # Remove pokemon2 at the start of the queue
                team_array_2.serve() # O(1)

                # Set new pokemon fighter for team 2, found at the front of the queue
                self.pokemon2 = team_array_2.array[team_array_2.front]

                # Rotate pokemon1 to the back in team 1 after defeating P2
                self.rotate(team_array_1) # O(1)

                # Set new pokemon fighter for team 2, found at the front of the queue
                self.pokemon1 = team_array_1.array[team_array_1.front]

            # If team array 1 is empty and glitch1 is true
            # This means that there is a MissingNo object left to fight for team 1
            # Therefore, create another queue of size 1 as the max MissingNo objects available
            # to fight for a team is 1. Then place this MissingNo object into the queue and let it fight
            # This same rule applies for team 2

            # This code only needs to run once after adding MissingNo to the queue/team,
            # Which is why we set glitched1 and glitched2 to True after
            # This same rule applies for team 2

            if team_array_1.is_empty() and glitch1 and glitched1 == False:
                self.queue = CircularQueue(1) # Create queue of size 1
                self.pokemon1 = MissingNo() # Create MissingNo() object named pokemon1
                self.queue.append(self.pokemon1) # O(1), Add pokemon1 to the queue
                team_array_1 = self.queue # O(1), # Name the queue as team1_array
                glitched1 = True
            if team_array_2.is_empty() and glitch2 and glitched2 == False:
                self.queue = CircularQueue(1) # Create queue of size 1
                self.pokemon2 = MissingNo() # Create MissingNo() object named pokemon2
                self.queue.append(self.pokemon2) # O(1), Add pokemon2 to the queue
                team_array_2 = self.queue # Name the queue as team2_array
                glitched2 = True

        # Rotate one more time for team 1 and team 2 as the front item may be duplicated again
        # after rotating and the last item in the queue may not look like it appears in the queue
        # after performing serve(). This case occurs when there are two items left in the queue
        # But the last item is actually still in the queue and is at the head of the queue
        # but the appearance of the queue may not be updated yet. Therefore, we're performing one last
        # rotation to update the queue

        if not team_array_1.is_empty() and len(team_array_1) == 2:
            team_array_1.serve() # O(1)
            team_array_1.append(self.pokemon1) # O(1)

        if not team_array_2.is_empty() and len(team_array_2) == 2:
            team_array_2.serve() # O(1)
            team_array_2.append(self.pokemon2) # O(1)

        # Announce the winner or draw
        if team_array_1.is_empty() and team_array_2.is_empty(): # O(1), If both teams are empty, It's a draw
            print("It's a draw")
            return "It's a draw"
        elif team_array_1.is_empty(): # If team 1 is empty, return team 2's name which is the winner
            print(self.team2.trainer_name)
            return self.team2.trainer_name
        elif team_array_2.is_empty(): # If team 2 is empty, return team 1's name which is the winner
            print(self.team1.trainer_name)
            return self.team1.trainer_name

    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) -> str:
        """
        The function optimised_mode_battle has the time complexity of O(m*(n+l)). The lines of code which are
        labelled constant has a constant time complexity whether it be O(n) or O(1) which does not affect the
        actual Big O notation of the whole function.

        This function takes in the users choice of input for attribute
        of the pokemon under the variable criterion. The teams are assigned based on the attributes and the pokemon
        in the array sorted list are than ordered based on those attributes in descending order. The pokemon from
        each team then battle in descending order based on the chosen attributes. The name of the player who wins
        is displayed.

        """

        print("Team 1:")
        # Set battle mode to 2 and let the user choose the team for team 1
        array = self.team1.choose_team(2, criterion_team1)  # Best and Worst Case O(n), constant
        total = array[0] + array[1] + array[2]  # array[0] = charm, array[1] = bulb, array[2] = squir

        # Check if the user has inputted a fourth value/MissingNo for team 1
        if array[3] == True and total < 6:
            glitch1 = True
        else:
            glitch1 = False

        # Create the team by placing the pokemons into the array/team 1
        team1_array = self.team1.assign_team(array[0], array[1], array[2])  # Best and Worst Case = O(n), constant

        print("Team 2:")
        # Set battle mode to 2 and let the user choose the team for team 1
        array = self.team2.choose_team(2, criterion_team2)  # Best and worst case = O(n)
        total = array[0] + array[1] + array[2]  # array[0] = charm, array[1] = bulb, array[2] = squir

        # Check if the user has inputted a fourth value/MissingNo for team 2
        if array[3] == True and total < 6:  # constant O(1)
            glitch2 = True # If a fourth value is found, Then there's a glitch for team 2
        else:
            glitch2 = False # If a fourth value is not found, then there's no glitch for team 2

        # Create the team by placing the pokemons into the array/team 2
        team2_array = self.team2.assign_team(array[0], array[1], array[2])  # Best and worst case = O(n)

        # Assign pokemon1 to fight for team 1 and pokemon2 to fight for team2
        # Where pokemon1 and pokemon2 are found at the end of the list
        pokemon1 = team1_array[team1_array.length - 1]  # O(1) constant
        pokemon2 = team2_array[team2_array.length - 1]  # O(1) constant

        # The reason why this code is here is explained later
        glitched1 = False
        glitched2 = False

        """
        This while loop checks if either team's array sorted list is empty, if not empty, the fight function
        is called to allow pokemon from both team to battle. If either is empty, proceed to display the name 
        of winner. The time complexity of the while loop below in big O notation would be O(n) for best and 
        worst case as the loop executes at least once which is still n amount of times while for worst case it is also 
        n amount of times ignoring the constant to get its Big O notation. Inside this while loop, there are 
        statement which calls poketype_sort and add function with Big O notations O(n) and O(l) for best and
        worst cases respectively given that l = len(self). The time complexity of the 2 functions would be
        the sum of each other in Big O notation. Hence, the time complexity of this loop including 
        other functions called inside it in Big O notation would be O(m*(n+l)).
        """

        while not team1_array.is_empty() and not team2_array.is_empty():  # O(m*(n+l)) where l = len(self)

            # Calculate damage and set_hp for the pokemons that are fighting
            self.fight(pokemon1.value, pokemon2.value)  # O(1) constant

            # if statements to check the criterion passed in by the user and determines the attribute accordingly
            # the attribute variables, attrb and attrb2 will be used to store key values
            # These if statements which check the attribute are all constant time,  O(1)
            if criterion_team1 == "hp":
                attrb = pokemon1.value.get_HP()
            elif criterion_team1 == "attack":
                attrb = pokemon1.value.get_attack()
            elif criterion_team1 == "level":
                attrb = pokemon1.value.get_level()
            elif criterion_team1 == "defence":
                attrb = pokemon1.value.get_defence()
            elif criterion_team1 == "speed":
                attrb = pokemon1.value.get_speed()

            if criterion_team2 == "hp":
                attrb2 = pokemon2.value.get_HP()
            elif criterion_team2 == "attack":
                attrb2 = pokemon2.value.get_attack()
            elif criterion_team2 == "level":
                attrb2 = pokemon2.value.get_level()
            elif criterion_team2 == "defence":
                attrb2 = pokemon2.value.get_defence()
            elif criterion_team2 == "speed":
                attrb2 = pokemon2.value.get_speed()

            """
            The code below checks if pokemon from each respective teams have HP more than 0. If it satisfies
            this condition, it updates the new key value of attribute of the pokemon and uses the add function
            to add the pokemon into the array sorted lists based on their updated key values at the right indexes.
            After adding the updated version of the pokemon, the old version of the pokemon which have battled are
            removed from the array sorted list. It then calls poketype_sort function to sort the pokemon based on
            the order Charmander->Bulbasaur->Squirtle if their key values are the same.
            
            The code below calls the poketype_sort function created with the Big O notation O(m) to sort
            the pokemon in the array sorted list based on their attributes. The if statements which are   
            labelled as constants are all have the time complexity of O(1) as they are in constant time
            The delete_at_index function is also having a constant time complexity which does not affect 
            the Big O Notation. It also calls the add function which have the best and worst case O(l) 
            where l = len(self). The best cases of first two calls do not align as when item is last,
            O(l)+ O(1) which gives O(l) while when item is first, O(1) + O(l) which gives O(l). 
            """
            if pokemon1.value.get_HP() > 0 and pokemon2.value.get_HP() > 0:  # constant
                # Decrease one hp when both pokemon are alive
                print("Both team 1's " + str((team1_array[team1_array.length - 1].value.NAME)) + " and team 2's " + str(
                    (team2_array[team2_array.length - 1].value.NAME)) + " are alive")

                if len(team1_array) > 1 and len(team2_array) > 1:  # constant
                    if attrb2 == team2_array[team2_array.length - 2].key:  # constant
                        pass
                    else:
                        pokemon2.key = attrb2  # constant
                        team2_array.add(pokemon2)  # O(l) where l = len(self)
                        team2_array.delete_at_index(team2_array.length - 1)  # constant
                        team2_array = self.poketype_sort(team2_array)  # best and worst case O(n)
                        pokemon2 = team2_array.array[team2_array.length - 1]

                    if attrb == team1_array[team1_array.length - 2].key:  # constant
                        pass
                    else:
                        pokemon1.key = attrb  # constant
                        team1_array.add(pokemon1)  # O(l) where l = len(self)
                        team1_array.delete_at_index(team1_array.length - 1)  # constant
                        team1_array = self.poketype_sort(team1_array)  # best and worst case O(n)
                        pokemon1 = team1_array.array[team1_array.length - 1]  # constant

            if pokemon1.value.get_HP() <= 0:
                print("team 1's " + str((team1_array[team1_array.length - 1].value.NAME)) + " gets fainted by team 2's "
                      + str(team2_array[team2_array.length - 1].value.NAME))

                team1_array.delete_at_index(team1_array.length - 1)  # constant
                pokemon1 = team1_array.array[team1_array.length - 1]  # constant
                if len(team2_array) > 1:
                    if attrb2 == team2_array[team2_array.length - 2].key:  # constant
                        pass
                    else:
                        pokemon2.key = attrb2  # constant
                        team2_array.add(pokemon2)  # O(l) where l = len(self)
                        team2_array.delete_at_index(team2_array.length - 1)  # constant
                        team2_array = self.poketype_sort(team2_array)  # best and worst case O(n)
                        pokemon2 = team2_array.array[team2_array.length - 1]  # constant

            # Check if health == 0 to remove the pokemon from the array sorted list
            if pokemon2.value.get_HP() <= 0:
                print("team 1's " + str((team1_array[team1_array.length - 1].value.NAME)) + " faints team 2's "
                      + str((team2_array[team2_array.length - 1].value.NAME)))

                team2_array.delete_at_index(team2_array.length - 1)
                pokemon2 = team2_array.array[team2_array.length - 1]
                if len(team1_array) > 1:
                    if attrb == team1_array[team1_array.length - 2].key:
                        pass
                    else:
                        pokemon1.key = attrb
                        team1_array.add(pokemon1)  # O(l) where l = len(self)
                        team1_array.delete_at_index(team1_array.length - 1)  # constant
                        team1_array = self.poketype_sort(team1_array)  # O(n)
                        pokemon1 = team1_array.array[team1_array.length - 1]

            # If team array 1 is empty and glitch1 is true
            # This means that there is a MissingNo object left to fight for team 1
            # Therefore, create another stack of size 1 as the max MissingNo objects available
            # to fight for a team is 1. Then place this MissingNo object into the stack and let it fight
            # This same rule applies for team 2

            # This code only needs to run once after adding MissingNo to the stack/team,
            # Which is why we set glitched1 and glitched2 to True after
            # This same rule applies for team 2

            if team1_array.is_empty() and glitch1 and glitched1 == False:
                self.array = ArraySortedList(1)  # Create array of size 1
                pokemon1 = MissingNo()  # Create MissingNo() object named pokemon1
                self.array.add(ListItem(pokemon1, attrb))  # Add pokemon1 to the array
                team1_array = self.array  # Name the array as team1_array
                pokemon1 = team1_array[team1_array.length - 1]  # pokemon1 is found at the end of the array
                glitched1 = True
            if team2_array.is_empty() and glitch2 and glitched2 == False:
                self.array = ArraySortedList(1)  # Create array of size 1
                pokemon2 = MissingNo()  # Create MissingNo() object named pokemon2
                self.array.add(ListItem(pokemon2, attrb2))  # Add pokemon2 to the array
                team2_array = self.array  # Name the array as team2_array
                pokemon2 = team2_array[team2_array.length - 1]  # pokemon2 is found at the end of the array
                glitched2 = True

        if team1_array.is_empty() and team2_array.is_empty():
            print("It's a draw")
            return "It's a draw"
        elif team1_array.is_empty():
            print(self.team2.trainer_name)
            return self.team2.trainer_name
        elif team2_array.is_empty():
            print(self.team1.trainer_name)
            return self.team1.trainer_name

# b = Battle("Ash", "Misty")
# result = b.set_mode_battle()
# print(b.team1)
# print(b.team2)

# b = Battle("Jack", "Taylor")
# b.rotating_mode_battle()
# print(b.team1)
# print(b.team2)

# b = Battle("Jack", "Taylor")
# result = b.optimised_mode_battle("hp", "level")
# print(b.team1)
# print(b.team2)

# b = PokeTeam("Jack")
# b.choose_team(0, None)
# print(str(b))

