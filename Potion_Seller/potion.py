class Potion:
    
    def __init__(self, potion_type: str, name: str, buy_price: float, quantity: float) -> None:
        """
        Potion object initialization, contains the type, name, buy price, and quantity
        Time Complexity is O(1)
        """
        self.potion_type = potion_type
        self.name = name
        self.buy_price = buy_price
        self.quantity = quantity

    @classmethod
    def create_empty(cls, potion_type: str, name: str, buy_price: float) -> 'Potion':
        """
        Class Method to create a Potion object with quantity 0
        Time Complexity is O(1)
        """
        return cls(potion_type,name,buy_price,0)

    @classmethod
    def good_hash(cls, potion_name: str, tablesize: int) -> int:
        """
        Uniform Hash function
        Takes into account all characters
        Uses varying coefficients for all characters
        """
        value = 0

        a = 31415
        b = 27183
        
        # a and b are coefficients chosen randomly (a = 31415, b = 27183)
        # where a is the base and b is the hash base

        for char in potion_name:
            value = (ord(char) + a * value) % tablesize
            # a is the noise or base that is applied here to every character  
            # which would help generate a random hash value in the end
            # and reduce the probability of a collision occuring
            a = a * b % (tablesize - 1) 
            # The base "a" will be updated randomly for each position 
        return value

        # This is a good hash function as it takes into account of all characters
        # and it will produce hash values in a way where there is less chance of a collision 

        # Table size must be a prime number because it will distribute the numbers in a better way
        # If the table size is not a prime number then there will be the concept of zero divisors
        # e.g. (4 * 3) % 6 
        # then the result would be 0 which is not what we want
        # because we would lose everything we calculated for the prefix of the word

    @classmethod
    def bad_hash(cls, potion_name: str, tablesize: int) -> int:
        """
        Returns the ASCII code of the first character modulo table size
        There are only 26 alphabet characters, so there will be many collisions and conflict
        Time Complexity is O(1)
        """
        return ord(potion_name[0]) % tablesize

        # This is a bad hash function because if the first letter of different potion names are the same
        # then these objects will have the same hash values which will cause collision

    def get_name(self) -> str:
        """
        Getter for a potion name
        Time Complexity is O(1)
        """
        return self.name

    def get_buy_price(self) -> float:
        """
        Getter for a potion buy price
        Time Complexity is O(1)
        """ 
        return self.buy_price

    def get_potion_type(self) -> str:
        """
        Getter for a potion type
        Time Complexity is O(1)
        """
        return self.potion_type
    
    def get_quantity(self) -> float:
        """
        Getter for the quantity of a potion object
        Time Complexity is O(1)
        """
        return self.quantity

    def set_quantity(self, new_quantity) -> bool:
        """
        Sets the quantity of a potion
        Time Complexity is O(1)
        """
        
        self.quantity = new_quantity

        return True
