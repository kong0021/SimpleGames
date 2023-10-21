""" 
Hash Table ADT

Defines a Hash Table using Linear Probing for conflict resolution.
It currently rehashes the primary cluster to handle deletion.
"""
__author__ = 'Brendon Taylor, modified by Jackson Goerner'
__docformat__ = 'reStructuredText'
__modified__ = '21/05/2020'
__since__ = '14/05/2020'

from referential_array import ArrayR
from typing import TypeVar, Generic
from primes import largest_prime
from potion import Potion
T = TypeVar('T')


class LinearProbePotionTable(Generic[T]):
    """
    Linear Probe Potion Table

    This potion table does not support deletion.

    attributes:
        count: number of elements in the hash table
        table: used to represent our internal array
        table_size: current size of the hash table
    """

    def __init__(self, max_potions: int, good_hash: bool=True, tablesize_override: int=-1) -> None:
        """
        Initialization of the hash table
        The hash table size can be overrode with the third argument, otherwise,
        it will choose an appropriate size based on the max potion amount.
        Time Complexity is O(1)
        """
        # Statistic setting
        self.conflict_count = 0
        self.probe_max = 0
        self.probe_total = 0
        #Instance Variables
        self.max_potions = max_potions
        self.good_hash = self.set_hash(good_hash)
        #Tablesize
        self.tablesize = self.set_tablesize(tablesize_override)
        self.count = 0
        self.table = ArrayR(self.tablesize)
        self.hash_values = []
    
    def set_hash(self, hash_type: bool)->bool:
        """
        Setter method for the hash function type
        Time Complexity is O(1)
        """
        if hash_type:
            return True
        return False

    def get_hash(self)-> bool:
        """
        Getter for what type of hash function we are currently using
        Time Complexity is O(1)
        """
        return self.good_hash
    
    def set_tablesize(self, tablesize_override: int) -> int:
        """
        If tablesize_override is -1, the method should choose an appropriate size according to max_potions
        Else, directly set hashtable size to the value given in tablesize_override
        We will multiply the max potions by 1.5 first because if we immediately use findLargestPrime, it might find a number
        too small and will not fit the potions.
        Time Complexity is O(log(log n)) because of largest_prime
        """
        if tablesize_override != -1:
            return tablesize_override
        else:
            findLargestPrime = self.max_potions * 1.5
            return largest_prime(int(findLargestPrime))
        
        # The hash table should be an array with length about 1.5 times the maximum number of keys that will 
        # actually be in the table, and size of hash table array should be a prime number.
    
    def get_tablesize(self) -> int:
        """
        Getter for the table size
        Time Complexity is O(1)
        """
        return self.tablesize

    def hash(self, potion_name: str) -> int:
        """
        If self.good_hash is True, use Potion.good_hash
        Else, use Potion.bad_hash
        """
        if self.get_hash():
            return Potion.good_hash(potion_name, self.get_tablesize())
        else:
            return Potion.bad_hash(potion_name, self.get_tablesize())

    def statistics(self) -> tuple:
        """
        Returns a tuple with three value:
        1. Total number of conflicts (self.conflict_count)
        2. Total distance probed throughout code execution (self.probe_total)
        3. Length of longest probe chain throughout code execution (self.probe_max)
        
        - Output of statistics method for good hash function:
          For the good hash function, it takes into account of all characters
          and it will produce hash values in a way where there is less chance of a collision occuring
        
          Therefore the values for conflict_count, probe_total, and probe_max is expected to be less than
          the bad hash function

          e.g. x => y (where x is the key and y is the hash value)
          a => 97
          aar => 175
          bi => 198
          ba => 163

          No collisions here so the expected output of statistics is:
          (0, 0, 0) -> (conflict_count, probe_total, probe_max)

        - Output of statistics method for bad hash function:
          For the bad hash function, it will only take into account of the first character of the string
          
          This is bad because if the first letter of different potion names are the same
          then these objects will have the same hash values and more collisions are likely to occur

          Therefore the values for conflict_count, probe_total, and probe_max is expected to be larger than
          the good hash function

          e.g. x => y (where x is the key and y is the hash value)
          a => 12
          aar => 12
          bi => 13
          ba => 13

          2 collisions here so the expected output of statistics is:
          (2, 2, 1) -> (conflict_count, probe_total, probe_max)

        """
        stats = (self.conflict_count, self.probe_total, self.probe_max)
        return stats

    def __len__(self) -> int:
        """
        Returns number of elements in the hash table
        :complexity: O(1)
        """
        return self.count

    def __linear_probe(self, key: str, is_insert: bool) -> int:
        """
        Find the correct position for this key in the hash table using linear probing
        :complexity best: O(K) first position is empty
                          where K is the size of the key
        :complexity worst: O(K + N) when we've searched the entire table
                           where N is the table_size
        :raises KeyError: When a position can't be found
        """
        position = self.hash(key)  # get the position using hash
        conflict = False
        probe_max_temp = 0

        if is_insert and self.is_full():
            raise KeyError(key)

        for _ in range(len(self.table)):  # start traversing
            if self.table[position] is None:  # found empty slot
                if is_insert:
                    if conflict == True:
                        self.conflict_count += 1
                        conflict = False
                    # If a conflict occurs (True) we increase conflict_count by 1
                    # Then reset conflict back to False after

                    if probe_max_temp > self.probe_max:
                        self.probe_max = probe_max_temp
                    # If the length of the probe chain (temp) that was calculated earlier is larger than
                    # the length of the current longest probe chain (probe_max_temp), then we will replace it with the temp value
                    return position
                else:
                    raise KeyError(key)  # so the key is not in
            elif self.table[position][0] == key:  # found key
                return position
            else:  # there is something but not the key, try next

                # It is here where Linear Probing occurs
                # Therefore we can increase the probe total here
                self.probe_total += 1 
                position = (position + 1) % len(self.table)

                # It is also here where we should keep count of the length of the probe chain
                # So a temp variable is created to keep track of it
                probe_max_temp += 1

                conflict = True
                # According to the definition of conflict:
                # A conflict happens when linear probing is required to find 
                # a position for the value being inserted
                # Therefore it is here where we set conflict to True

        raise KeyError(key)

    def __contains__(self, key: str) -> bool:
        """
        Checks to see if the given key is in the Hash Table
        :see: #self.__getitem__(self, key: str)
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: str) -> T:
        """
        Get the item at a certain key
        :see: #self.__linear_probe(key: str, is_insert: bool)
        :raises KeyError: when the item doesn't exist
        """
        position = self.__linear_probe(key, False)
        return self.table[position][1]

    def __setitem__(self, key: str, data: T) -> None:
        """
        Set an (key, data) pair in our hash table
        :see: #self.__linear_probe(key: str, is_insert: bool)
        :see: #self.__contains__(key: str)
        """
        if len(self) == len(self.table) and key not in self:
            raise ValueError("Cannot insert into a full table.")
        position = self.__linear_probe(key, True)
        self.hash_values.append(position)

        if self.table[position] is None:
            self.count += 1
        self.table[position] = (key, data)

    def initalise_with_tablesize(self, tablesize: int) -> None:
        """
        Initialise a new array, with table size given by tablesize.
        Complexity: O(n), where n is len(tablesize)
        """
        self.count = 0
        self.table = ArrayR(tablesize)

    def is_empty(self)-> bool:
        """
        Returns whether the hash table is empty
        :complexity: O(1)
        """
        return self.count == 0

    def is_full(self):
        """
        Returns whether the hash table is full
        :complexity: O(1)
        """
        return self.count == len(self.table)

    def insert(self, key: str, data: T) -> None:
        """
        Utility method to call our setitem method
        :see: #__setitem__(self, key: str, data: T)
        """
        self[key] = data

    def remove(self, key: str) -> None:
        """
        Utility method to call our setitem method
        :see: #__setitem__(self, key: str, data: T)
        """
        self[key] = None

    def __str__(self) -> str:
        """
        Returns all they key/value pairs in our hash table (no particular order)
        :complexity: O(N) where N is the table size
        """
        result = ""
        for item in self.table:
            if item is not None:
                (key, value) = item
                result += "(" + str(key) + "," + str(value) + ")\n"
        return result



# lookup = {
#     "s1": 5,
#     "s2": 5,
#     "s3": 5,
#     "s4": 7
# }
# h = lambda self, k: lookup[k]
# saved = LinearProbePotionTable.hash
# LinearProbePotionTable.hash = h
# # What the above code does is essentially work around using good_hash or bad hash.
# # This is the example given in the section on conflict and probe counting
# l = LinearProbePotionTable(10, True, 10)
# l["s1"] = "s1"
# l["s2"] = "s2"
# l["s3"] = "s3"

# print(l.table[5])

