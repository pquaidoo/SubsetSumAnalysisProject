'''Driver

    program tests 3 different algorithims for Subset Sum which returns a boolean if there is a sequence that adds up to a target number.
    The driver calculates how long each algorithim takes, and how much table space was used, it will also tell whether each algorithim matches
    the boolean inputed, and shows the subsequence created by the algorthims.
  Input: 
      int n:length of sequence, 
      int r: upper bound of numbers in sequence, 
      boolean, v: if sequence should return true or false
  Output: 
      Each Algorithim:
      Result Boolean
      Time in milliseconds
      Table space used
      String of sum sequence that equals the target
'''
def driver():
    print("Driver function is running")
    list1 = [1,4,2]
    answer = [[],False]
    check = bruteForceAlgo(list1, 8)
    print(check)

"""
Finds Subset sum in O(2^n) by creating a list of all possible subsets and iterates through list. 
If there is a sum, will return the elements in a list that add up to the target, and True boolean
if not it will return an empty array with a False boolean
Input list: list of integers to check, int: target sum
Output list: [list: sublist that adds up to target, boolean: True if there is a sublist that adds up to sum, False if not]
"""
def bruteForceAlgo(nums:list, target:int ):
    result = []
    
    def listOfSubset(index, path):
        if index == len(nums):
            result.append(path)
            return
        
        listOfSubset(index + 1, path + [nums[index]])
        
        listOfSubset(index + 1, path)
    
    listOfSubset(0, [])

    for i in result:
        if sum(i) == target:
            return [i,True]

    return [[],False]
 

def DynamicProgramingAlgo():
    pass
def CleverAlgo():
    pass



if __name__ == "__main__":  
    driver()

