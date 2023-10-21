from abc import ABC, abstractmethod


class PokemonBase(ABC):
    """
    The base class for all pokemon, giving each pokemon hp, poke_type, and a base level of 1.
    Includes basic methods for all pokemons
    """

    BASE_LEVEL = 1
    POKE_TYPES = ["Fire", "Water", "Grass", "None"]

    def __init__(self, hp: int, poke_type: str) -> None:
        assert poke_type in PokemonBase.POKE_TYPES
        self.hp = hp
        self.poke_type = poke_type
        self.level = PokemonBase.BASE_LEVEL

    def set_HP(self, hp: int) -> None:
        """
        Function used to set the hp of a Pokemon
        Time complexity is O(1)
        """
        self.hp = int(hp)

    def get_HP(self) -> int:
        """
        Function used to get the hp of a Pokemon
        Time complexity is O(1)
        """
        return self.hp

    def set_level(self, level: int) -> None:
        """
        Function used to set the level of a Pokemon
        Time complexity is O(1)
        """
        assert type(level) == int and level > 0, "Level must be a positive integer"
        self.level = level

    def get_level(self) -> int:
        """
        Function used to get the level of a Pokemon
        Time complexity is O(1)
        """
        return self.level

    def level_up(self) -> None:
        """
        Function can be used to level up Pokemon during battle by 1
        Time complexity is O(1)
        """
        self.level += 1

    def get_poke_type(self) -> str:
        """
        Function used to get the Poke Type of a Pokemon
        Time complexity is O(1)
        """
        return self.poke_type

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_speed(self) -> int:
        pass

    @abstractmethod
    def get_attack(self) -> int:
        pass

    @abstractmethod
    def get_defence(self) -> int:
        pass

    @abstractmethod
    def calculate_attacked_damage(self) -> int:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
