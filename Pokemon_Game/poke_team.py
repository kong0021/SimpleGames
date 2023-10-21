from queue_adt import CircularQueue
from stack_adt import ArrayStack
from array_sorted_list import ArraySortedList
from pokemon import Charmander, Bulbasaur, Squirtle, MissingNo
from sorted_list import ListItem


class PokeTeam:
    TEAM_LIMIT = 6

    def __init__(self, name):
        """
        Constructor method for PokeTeam class.
        Instance variables include ADTs that will be used later according to its battle mode
        Time complexity is O(1)
        """
        self.trainer_name = name
        self.battle_mode = 0
        self.queue = CircularQueue(0)
        self.stack = ArrayStack(0)
        self.array = ArraySortedList(0)

    def set_battle_mode(self, battle_mode: int):
        """
        Function to ask user input for battle mode
        Time complexity is O(1)
        """
        self.battle_mode = battle_mode

    def get_battle_mode(self) -> int:
        """
        Function to get the current battle mode
        Time complexity is O(1)
        """
        return self.battle_mode

    def choose_team(self, battle_mode: int = 0, criterion: str = None):
        """
        Function to ask user input for the pokemon team
        Best = O(1), first user input is correct
        Worst = O(N), n is the number of wrong user inputs
        """
        valid_team_input = False
        while valid_team_input == False:
            try:
                input_team = input(
                    "Howdy Trainer! Choose your team as C B S\nwhere C is the number of Charmanders\nB is the number of Bulbasaurs\nS is the number of Squirtles\n"
                )
                team_list = input_team.split(" ")
                for i in range(len(team_list)):
                    team_list[i] = int(team_list[i])

            except ValueError:
                print("Invalid team input. Number only separated with space!")
                continue

            if len(team_list) == 3:
                team_list.append(0)

            if sum(team_list) > PokeTeam.TEAM_LIMIT:
                print("Team limit is 6 pokemon!\n")
                continue

            if isinstance(team_list[3], int):
                if team_list[3] > 1:
                    print("Maximum MissingNo is 1\n")
                    continue

            if team_list[3] != None and team_list[3] == 1:
                glitch = True
            else:
                glitch = False
            print("Valid team input")
            charm, bulb, squir = team_list[0], team_list[1], team_list[2]
            valid_team_input = True

        self.set_battle_mode(battle_mode)

        self.criterion = criterion

        self.assign_team(charm, bulb, squir)

        return charm, bulb, squir, glitch

    def assign_team(self, charm: int, bulb: int, squir: int):
        """
        Function to assign team into the correct ADTs according to the battle mode
        Best time complexity is O(n)
        Worst time complexity is O(n)
        """
        assert charm + bulb + squir <= 6, "Pokemon team limit is 6"
        total = charm + bulb + squir

        # If the battle mode is 0, we use a stack ADT to create the team
        if self.get_battle_mode() == 0:
            # Since a stack is last in first out (LIFO)
            # We add Charmanders at the end of the list followed by Bulbasaurs and Squirtles
            # So if one of the pokemons at the end of the list faints, we can use the method pop
            # to remove the pokemon from the list
            self.stack = ArrayStack(total)
            for i in range(1, squir + 1):
                self.stack.push(Squirtle())
            for i in range(1, bulb + 1):
                self.stack.push(Bulbasaur())
            for i in range(1, charm + 1):
                self.stack.push(Charmander())

        # If the battle mode is 1, we use a circular queue ADT to create the team
        elif self.get_battle_mode() == 1:
            # Since a queue is last in first out (FIFO)
            # We add Charmanders at the start of the queue followed by Bulbasaurs and Squirtles
            # So if one of the pokemons at the start of the queue faints, we can use the method serve()
            # to remove the pokemon from the queue
            self.queue = CircularQueue(total)
            for i in range(1, charm + 1):
                self.queue.append(Charmander())
            for i in range(1, bulb + 1):
                self.queue.append(Bulbasaur())
            for i in range(1, squir + 1):
                self.queue.append(Squirtle())

        # If the battle mode is 2, we use a sorted array list ADT to create the team
        # ListItem of objects are added into an array sorted list based on the criterions for each team
        elif self.get_battle_mode() == 2:
            self.array = ArraySortedList(total)
            if self.criterion == "hp":
                for i in range(1, charm + 1):
                    self.array.add(
                        ListItem(Charmander(), Charmander().get_HP())
                    )
                for i in range(1, bulb + 1):
                    self.array.add(
                        ListItem(Bulbasaur(), Bulbasaur().get_HP())
                    )
                for i in range(1, squir + 1):
                    self.array.add(
                        ListItem(Squirtle(), Squirtle().get_HP())
                    )

            if self.criterion == "attack":
                for i in range(1, charm + 1):
                    self.array.add(
                        ListItem(Charmander(), Charmander().get_attack())
                    )
                for i in range(1, bulb + 1):
                    self.array.add(
                        ListItem(Bulbasaur(), Bulbasaur().get_attack())
                    )
                for i in range(1, squir + 1):
                    self.array.add(
                        ListItem(Squirtle(), Squirtle().get_attack())
                    )

            if self.criterion == "level":
                for i in range(1, charm + 1):
                    self.array.add(
                        ListItem(Charmander(), Charmander().get_level())
                    )
                for i in range(1, bulb + 1):
                    self.array.add(
                        ListItem(Bulbasaur(), Bulbasaur().get_level())
                    )
                for i in range(1, squir + 1):
                    self.array.add(
                        ListItem(Squirtle(), Squirtle().get_level())
                    )

            if self.criterion == "defence":
                for i in range(1, charm + 1):
                    self.array.add(
                        ListItem(Charmander(), Charmander().get_defence())
                    )
                for i in range(1, bulb + 1):
                    self.array.add(
                        ListItem(Bulbasaur(), Bulbasaur().get_defence())
                    )
                for i in range(1, squir + 1):
                    self.array.add(
                        ListItem(Squirtle(), Squirtle().get_defence())
                    )

            if self.criterion == "speed":
                for i in range(1, charm + 1):
                    self.array.add(
                        ListItem(Charmander(), Charmander().get_speed())
                    )
                for i in range(1, bulb + 1):
                    self.array.add(
                        ListItem(Bulbasaur(), Bulbasaur().get_speed())
                    )

                for i in range(1, squir + 1):
                    self.array.add(
                        ListItem(Squirtle(), Squirtle().get_speed())
                    )

        # Now return the suitable ADT
        if self.get_battle_mode() == 0: # If the battle mode is 0, return the stack ADT
            return self.stack
        elif self.get_battle_mode() == 1: # If the battle mode is 1, return the circular queue ADT
            return self.queue
        elif self.get_battle_mode() == 2: # If the battle mode is 2, return the sorted array list ADT
            return self.array

    def __str__(self) -> str:
        """
        Overall time complexity = O(N)
        What this method consists of:
        1. for loop - Best: O(1) if the user has one input/pokemon, Worst: O(N) if the user has more than one input/pokemon

        Best time complexity = O(N)
        Worst time complexity = O(N)

        Print the hp and level of each pokemon in the team
        """

        retVal = ""

        if self.get_battle_mode() == 0:
            retVal = ", ".join(str(pokemon) for pokemon in self.stack.array[::-1])

            return retVal

        elif self.get_battle_mode() == 1:
            for i in range(self.queue.length - 1):
                retVal += str(self.queue.array[i]) + ", "
            retVal += str(self.queue.array[self.queue.length - 1])
            return retVal

        elif self.get_battle_mode() == 2:
            for i in range(self.array.length - 1):
                retVal += str(self.array.array[i].value) + ", "
            retVal += str(self.array.array[self.array.length - 1].value)
            return retVal




# b = PokeTeam("Ash")
# b.choose_team(0, None)
# print(str(b))


# print(b.team)
