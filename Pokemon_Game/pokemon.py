from abc import abstractmethod
from pokemon_base import PokemonBase


class Charmander(PokemonBase):
    """
    Class for Charmander pokemon
    """

    NAME = "Charmander"
    HP = 7
    POKE_TYPE = "Fire"
    TYPE_EFFECTIVENESS = {"Fire": 1, "Water": 0.5, "Grass": 2, "None": 1}
    ATTACK = 6
    DEFENCE = 4
    SPEED = 7

    def __init__(self) -> None:
        """
        Constructor method for Charmander Pokemon
        Time complexity is always O(1)
        """
        PokemonBase.__init__(self, Charmander.HP, Charmander.POKE_TYPE)
        self.attack = Charmander.ATTACK + self.level
        self.defence = Charmander.DEFENCE
        self.speed = Charmander.SPEED + self.level

    def get_name(self) -> str:
        """
        Function used to get the name of Charmander pokemon. Uses class variable because it is the same for all instance
        Time complexity is always O(1)
        """
        return self.NAME

    def get_attack(self) -> int:
        """
        Function used to get the attack value of a Charmander pokemon. Instance variable because it may change with level
        Time complexity is always O(1)
        """
        return self.attack

    def get_defence(self) -> int:
        """
        Function used to get the defence value of a Charmander pokemon. Instance variable because it may change with level
        Time complexity is always O(1)
        """
        return self.defence

    def get_speed(self) -> int:
        """
        Function used to get the speed value of a Charmander pokemon. Instance variable because it may change with level
        Time complexity is always O(1)
        """
        return self.speed

    def calculate_attacked_damage(self, opponent) -> int:
        """
        Function takes another Pokemon object as argument.
        The function will calculate how much damage the opponent deals to self pokemon.
        Takes opponent attack value, opponent type effectiveness and self pokemon defence into account.
        Time complexity is always O(1)
        """
        effective_damage = (
            opponent.get_attack() * opponent.TYPE_EFFECTIVENESS[self.poke_type]
        )
        if effective_damage > self.defence:
            self.set_HP(self.hp - effective_damage)
        else:
            self.set_HP(self.hp - effective_damage // 2)
        return self.hp

    def __str__(self) -> str:
        return f"{self.NAME}'s HP = {self.hp} and level = {self.level}"


class Bulbasaur(PokemonBase):
    """
    Class for pokemon Bulbasaur
    """

    NAME = "Bulbasaur"
    HP = 9
    POKE_TYPE = "Grass"
    TYPE_EFFECTIVENESS = {"Fire": 0.5, "Water": 2, "Grass": 1, "None": 1}
    ATTACK = 5
    DEFENCE = 5
    SPEED = 7

    def __init__(self) -> None:
        """
        Constructor method for Bulbasaur Pokemon
        Time complexity is always O(1)
        """
        PokemonBase.__init__(self, Bulbasaur.HP, Bulbasaur.POKE_TYPE)
        self.attack = Bulbasaur.ATTACK
        self.defence = Bulbasaur.DEFENCE
        self.speed = Bulbasaur.SPEED + (self.level // 2)

    def get_name(self) -> str:
        """
        Function used to get the name of Squirtle pokemon. Uses class variable because it is the same for all instance
        Time complexity is always O(1)
        """
        return self.NAME

    def get_attack(self) -> int:
        """
        Function used to get the attack value of a Squirtle pokemon. Instance variable because it may change with level
        Time complexity is always O(1)
        """
        return self.attack

    def get_defence(self) -> int:
        """
        Function used to get the defence value of a Squirtle pokemon. Instance variable because it may change with level
        Time complexity is always O(1)
        """
        return self.defence

    def get_speed(self) -> int:
        """
        Function used to get the speed value of a Squirtle pokemon. Instance variable because it may change with level
        Time complexity is always O(1)
        """
        return self.speed

    def calculate_attacked_damage(self, opponent) -> int:
        """
        Function takes another Pokemon object as argument.
        The function will calculate how much damage the opponent deals to self pokemon.
        Takes opponent attack value, opponent type effectiveness and self pokemon defence into account.
        Time complexity is always O(1)
        """
        effective_damage = (
            opponent.get_attack() * opponent.TYPE_EFFECTIVENESS[self.poke_type]
        )
        if effective_damage > self.defence + 5:
            self.set_HP(self.hp - effective_damage)
        else:
            self.set_HP(self.hp - effective_damage // 2)
        return self.hp

    def __str__(self) -> str:
        return f"{self.NAME}'s HP = {self.hp} and level = {self.level}"


class Squirtle(PokemonBase):
    """
    Class for pokemon Squirtle
    """

    NAME = "Squirtle"
    HP = 8
    POKE_TYPE = "Water"
    TYPE_EFFECTIVENESS = {"Fire": 2, "Water": 1, "Grass": 0.5, "None": 1}
    ATTACK = 4
    DEFENCE = 6
    SPEED = 7

    def __init__(self) -> None:
        """
        Constructor method for Squirtle Pokemon
        Time complexity is always O(1)
        """
        PokemonBase.__init__(self, Squirtle.HP, Squirtle.POKE_TYPE)
        self.attack = Squirtle.ATTACK + (self.level // 2)
        self.defence = Squirtle.DEFENCE + self.level
        self.speed = Squirtle.SPEED

    def get_name(self) -> str:
        """
        Function used to get the name of Squirtle pokemon. Uses class variable because it is the same for all instance
        Time complexity is always O(1)
        """
        return self.NAME

    def get_attack(self) -> int:
        """
        Function used to get the attack value of a Squirtle pokemon. Instance variable because it may change with level
        Time complexity is always O(1)
        """
        return self.attack

    def get_defence(self) -> int:
        """
        Function used to get the defence value of a Squirtle pokemon. Instance variable because it may change with level
        Time complexity is always O(1)
        """
        return self.defence

    def get_speed(self) -> int:
        """
        Function used to get the speed value of a Squirtle pokemon. Instance variable because it may change with level
        Time complexity is always O(1)
        """
        return self.speed

    def calculate_attacked_damage(self, opponent) -> int:
        """
        Function takes another Pokemon object as argument.
        The function will calculate how much damage the opponent deals to self pokemon.
        Takes opponent attack value, opponent type effectiveness and self pokemon defence into account.
        Time complexity is always O(1)
        """
        effective_damage = (
            opponent.get_attack() * opponent.TYPE_EFFECTIVENESS[self.poke_type]
        )
        if effective_damage > self.defence * 2:
            self.set_HP(self.hp - effective_damage)
        else:
            self.set_HP(self.hp - effective_damage // 2)
        return self.hp

    def __str__(self) -> str:
        return f"{self.NAME}'s HP = {self.hp} and level = {self.level}"


# random will be used for some functions in GlitchMon and MissingNo
import random


class GlitchMon(PokemonBase):
    """
    Abstract class GlitchMon that will later be used for MissingNo
    """

    TYPE_EFFECTIVENESS = {"Fire": 1, "Water": 1, "Grass": 1, "None": 1}

    def __init__(self) -> None:
        """
        constructor for GlitchMon class. Dont need to have any paraameters for this one.
        There is no best and worst case for this one. Overall time complexity will be O(1).
        """
        PokemonBase.__init__(
            self,
            (Squirtle().get_HP() + Charmander().get_HP() + Bulbasaur().get_HP()) // 3,
            "None",
        )
        self.attack = None
        self.name = None
        self.defence = None
        self.speed = None

    def set_speed(self, speed):
        self.speed = speed

    def set_attack(self, attack):
        self.attack = attack

    def get_hp(self):
        return self.hp

    def get_name(self) -> str:
        """
        getter for name. Dont need to have any paraameters for this one, it will return the name of MissingNO pokemon
        There is no best and worst case for this one. Overall time complexity will be O(1).
        """
        return self.name

    def get_attack(self) -> int:
        """
        getter for attack. Dont need to have any paraameters for this one, it will return the attack of MissingNO pokemon
        There is no best and worst case for this one. Overall time complexity will be O(1).
        """
        return self.attack

    def get_defence(self) -> int:
        """
        getter for defence. Dont need to have any paraameters for this one, it will return the defence of MissingNO pokemon
        There is no best and worst case for this one. Overall time complexity will be O(1).
        """
        return self.defence

    def get_speed(self) -> int:
        """
        getter for speed. Dont need to have any paraameters for this one, it will return the speed of MissingNO pokemon
        There is no best and worst case for this one. Overall time complexity will be O(1).
        """
        return self.speed

    @abstractmethod
    def calculate_attacked_damage(self, opponent) -> int:
        """
        An abstract method to calculate the damage. Will be imlemented in MissingNo class
        There is no best and worst case for this one. Overall time complexity will be O(1).
        """
        pass

    @abstractmethod
    def hp_increaser(self):
        """
        An abstract method to increase the HP by 1.
        There is no best and worst case for this one. Overall time complexity will be O(1).
        """
        pass

    @abstractmethod
    def superpower(self):
        """
        An abstract method Missing No.
        There is no best and worst case for this one. Overall time complexity will be O(1).
        """
        pass

    def __str__(self) -> str:
        return f"{self.get_name()}'s HP = {self.hp} and level = {self.level}"


class MissingNo(GlitchMon):
    """
    Class for MissingNo Pokemon, inheriting GlitchMon
    """

    NAME = "MissingNo"
    TYPE_EFFECTIVENESS = {"Fire": 1, "Water": 1, "Grass": 1, "None": 1}

    def __init__(self) -> None:
        """
        Constructor for Missing No.
        There is no best and worst case for this one. Overall time complexity will be O(1).
        """
        GlitchMon.__init__(self)
        self.name = MissingNo.NAME
        self.attack = (Squirtle().ATTACK + Charmander().ATTACK + Bulbasaur().ATTACK) / 3
        self.defence = (
            Squirtle().DEFENCE + Charmander().DEFENCE + Bulbasaur().DEFENCE
        ) / 3
        self.speed = (Squirtle().SPEED + Charmander().SPEED + Bulbasaur().SPEED) / 3

    def level_up(self) -> None:
        """
        Increase the level og MissingNo by 1 and scale each stat by 1.
        There is no best and worst case for this one. Overall time complexity will be O(1).
        """
        self.level += 1
        self.hp_increaser()
        self.attack += 1
        self.speed += 1
        self.defence += 1

    def superpower(self):
        """
        a special method for the missing no. it will randomly choose a buff for MissingNo.
        There is no best and worst case for this one. Overall time complexity will be O(1).
        """
        power = ["1 Lvl", "1 HP", "1 HP and 1 Lvl"]
        choice = random.choice(power)
        if choice == "1 Lvl":
            self.level_up()
        elif choice == "1 HP":
            self.hp_increaser()
        else:
            self.level_up()
            self.hp_increaser()

    def hp_increaser(self):
        """
        Increase the HP of the MissingNo
        There is no best and worst case for this one. Overall time complexity will be O(1).
        """
        self.set_HP(self.hp + 1)

    def calculate_attacked_damage(self, opponent) -> int:
        """
        MissingNo can use all of the pokemon damage calculation type. Thus, each of them will have 1/3 chances to be used.
        When this function is being called it means that MissingNo is being attacked so it could call its superpower function also which has 25% to happen.
        There is no best and worst case for this one. Overall time complexity will be O(1).
        """
        # overriding this method from base class.
        effective_damage = opponent.get_attack() * 1
        defend_type = [1, 2, 3]
        ran_type = random.choice(defend_type)  # CHANGE
        if ran_type == 1:  # CHNAGE
            if effective_damage > self.get_defence() * 2:
                self.set_HP(self.get_HP() - effective_damage)
            else:
                self.set_HP(self.get_HP() - effective_damage // 2)
        elif ran_type == 2:  # CHANGE
            if effective_damage > self.get_defence() * 2:
                self.set_HP(self.get_HP() - effective_damage)
            else:
                self.set_HP(self.get_HP() - effective_damage // 2)
        else:
            if effective_damage > self.get_defence():
                self.set_HP(self.get_HP() - effective_damage)
            else:
                self.set_HP(self.get_HP() - effective_damage // 2)

        if random.random() > 0.75:  # 25% chances of callling superpower
            self.superpower()

        return self.get_HP()


# mn = MissingNo()
# print(mn.get_name())

# MissingNo1 = MissingNo()
# charmander1 = Charmander()
# charmander2 = Charmander()
# bulbasaur1 = Bulbasaur()
# bulbasaur2 = Bulbasaur()
# squirtle1 = Squirtle()
# charmander1.set_level(2)
# print(squirtle1.calculate_attacked_damage(charmander1))
# print(charmander1.calculate_attacked_damage(squirtle1))
# print(squirtle1.get_HP())
# print(charmander1.get_HP())

# squirtle2 = Squirtle()

# print(charmander1)
# print(charmander1.get_name())  # "Charmander"
# print(charmander1.get_poke_type())  # "Fire"
# print(charmander1.get_HP())  # 7
# print(charmander1.get_attack())  # 6 + level
# print(charmander1.get_defence())  # 4
# print(charmander1.get_speed())  # 7 + level
# print(charmander1.get_level())  # 1
# print(
#     charmander1.calculate_attacked_damage(charmander2)
# )  # 7 * 1 = 7. damage > defence. hp = 7 - 7 = 0
# print(
#     charmander1.calculate_attacked_damage(bulbasaur2)
# )  # 5 * 0.5 = 2.5. damage < defence. hp = 0 - 1 = -1
# print(
# charmander1.calculate_attacked_damage(squirtle2)
# )  # 4 * 2 = 8. damage > defence. -1 - 8 = -9

# print("\n")

# print(bulbasaur1)
# print(bulbasaur1.get_name())
# print(bulbasaur1.get_poke_type())
# print(bulbasaur1.get_HP())
# print(bulbasaur1.get_attack())
# print(bulbasaur1.get_defence())
# print(bulbasaur1.get_speed())
# print(bulbasaur1.get_level())
# print(
#     bulbasaur1.calculate_attacked_damage(charmander2)
# )  # 7 * 2 = 14. damage > defence + 5. 9 - 14 = -5
# print(
#     bulbasaur1.calculate_attacked_damage(bulbasaur2)
# )  # 5 * 1 = 5. damage < defence + 5. -5 - 2 = -7
# print(
# bulbasaur1.calculate_attacked_damage(squirtle2)
# )  # 4 * 0.5 = 2. damage < defence + 5. -7 -1 = -8

# print("\n")

# print(squirtle1)
# print(squirtle1.get_name())
# print(squirtle1.get_poke_type())
# print(squirtle1.get_HP())
# print(squirtle1.get_attack())
# print(squirtle1.get_defence())
# print(squirtle1.get_speed())
# print(squirtle1.get_level())
# print(
#     squirtle1.calculate_attacked_damage(charmander2)
# )  # 7 * 0.5 = 3.5. damage < defence*2. hp = 8 - 1 = 7
# print(
#     squirtle1.calculate_attacked_damage(bulbasaur2)
# )  # 5 * 2 = 10. damage < defence*2 . hp = 7 - 5 = 2
# print(
#     squirtle1.calculate_attacked_damage(squirtle2)
# )  # 4 * 1 = 4. damage < defence*2. hp = 2 - 2 = 0

# print("\n")

# print(MissingNo1)
# print(MissingNo1.get_name())
# print(MissingNo1.get_poke_type())
# print(MissingNo1.get_HP())
# print(MissingNo1.get_attack())
# print(MissingNo1.get_defence())
# print(MissingNo1.get_speed())
# print(MissingNo1.get_level())
# print(
#     MissingNo.calculate_attacked_damage(charmander2)
# )  # 7 * 0.5 = 3.5. damage < defence*2. hp = 8 - 1 = 7
# print(
#     MissingNo1.calculate_attacked_damage(bulbasaur1)
# )  # The defence type will be one of the three defence type
# print(
#     MissingNo1.calculate_attacked_damage(squirtle1)
# )  # The defence type will be one of the three defence type
# print(
#     MissingNo1.calculate_attacked_damage(charmander1)
# )  # The defence type will be one of the three defence type
