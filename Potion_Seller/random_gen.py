from typing import Generator

def lcg(modulus: int, a: int, c: int, seed: int) -> Generator[int, None, None]:
    """Linear congruential generator."""
    while True:
        seed = (a * seed + c) % modulus
        yield seed

class RandomGen:
    """
    Class to make the Randomly Generated Number
    """
    def __init__(self, seed: int=0) -> None:
        """
        Class initialization, contains seed and generator from lcg function.
        Time Complexity is O(1)
        """
        self.seed = seed
        self.random_gen = lcg(pow(2,32), 134775813,1, self.get_seed())
    
    def get_seed(self)->int:
        """
        Getter for the seed of the object.
        Time Complexity is O(1)
        """
        return self.seed

    def randint(self, k: int) -> int:
        """
        Method to generate a random number with a very specific approach.
        1. Get 5 random decimal number from the lcg method
        2. Convert it to binary
        3. Remove 16 Least Significant Bits if the number is longer than 16 bits
        4. Pad the numbers so every number is the same length
        5. Create a new binary number, where it is a 1 when there are at least 3 1s from the previously generated number
        6. Convert it to decimal, modulo k (input number) + 1
        7. Return the generated number
        Time Complexity is O(k) where k is the length of the string after slicing
        """
        #List to contain 5 number
        random_num = []
        
        #Get 5 number from the random_gen and put it in random_num
        for _ in range(5):
            #Take a number from the random gen and convert it to binary
            num = bin(next(self.random_gen))
            #Append it to random num
            random_num.append(num[2:])

        #Check if length of num is greater than 16, if yes, remove 16 Least Significant Bits
        #Else, do nothing
        for i in range(len(random_num)):
            num_string = random_num[i]
            if len(random_num[i])>16:
                random_num[i] = random_num[i][:len(num_string)-16]
        
        #Make the length all the same to index later for counting 1s in index.
        #max_length = Length of longest number
        max_length = len(max(random_num,key=len))
        for i in range(len(random_num)):
            if len(random_num[i])!=max_length:
                random_num[i] = random_num[i].zfill(max_length)
            # print(random_num[i])

        #Using indexing to check how many 1s is in an index, because currently, random num elements
        #are string, so we can index it.
        new_num = ""
        for i in range(max_length):
            count = 0
            for j in range(len(random_num)):
                if random_num[j][i] == '1':
                    count+=1
            if count >= 3:
                new_num+='1'
            else:
                new_num+='0'

        #Convert to decimal, modulo k plus 1 and return
        new_num = int(new_num, 2) % k + 1
        return new_num


        
# rgen = RandomGen()
# print(rgen.randint(100))

if __name__ == "__main__":
    Random_gen = lcg(pow(2,32), 134775813, 1, 0)
