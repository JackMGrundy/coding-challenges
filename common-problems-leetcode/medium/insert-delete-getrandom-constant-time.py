"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
Accepted
108,552
Submissions
255,048
"""

"""
Hash table...
use hashfunction that hashes to range of 0-16...
double whenever full...
For random selection...select a random val in the range...check is the slot is taken...if not...try again until a hit
"""

# 112ms. 94th percentile.
# Burned through this with a very tired mind...realized after the fact a stack would be a bit better...
# not worrying about it now...looks like its still fast at least...
from random import choice
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.valsToIds = {}
        self.IdsToVals = {}
        self.nextIDToAssign = 0
        self.smallestId = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.valsToIds:
            return False
        
        self.valsToIds[val] = self.nextIDToAssign
        self.IdsToVals[self.nextIDToAssign] = val
        self.nextIDToAssign += 1
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.valsToIds:
            return False
        
        valIdToDelete = self.valsToIds[val]
        del self.IdsToVals[valIdToDelete]
        del self.valsToIds[val]
        
        if valIdToDelete == self.smallestId:
            self.smallestId += 1
            return True
        else:
            replacementVal = self.IdsToVals[self.smallestId]
            del self.IdsToVals[self.smallestId]
            del self.valsToIds[replacementVal]
            self.smallestId += 1
        
            self.IdsToVals[valIdToDelete] = replacementVal
            self.valsToIds[replacementVal] = valIdToDelete
            

            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.smallestId == self.nextIDToAssign:
            return None
        return self.IdsToVals[choice(range(self.smallestId, self.nextIDToAssign))]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()