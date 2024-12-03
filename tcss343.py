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

      makes a array of n length
      put n random positive integers ranging from 1 - r in array
      if boolean is true, randomly choose indexes and get sum of said index and make it the target
      if boolean is false, adds all 

'''
def driver():
    print("Driver function is running")
    list1 = [1,4,2]
    answer = [[],False]
    check = bruteForceAlgo(list1, 8)
    print(check)
    list2 = [1,2,3]
    check = DynamicProgramingAlgo(list2, 0)
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
 

def DynamicProgramingAlgo(nums:list, target:int ):
    My_Table = [[False] * (target + 1) for _ in range(len(nums))] # creates a 2d array with false in each index
    res = [] # is the result
    for i in range(len(nums)): # makes first column all true
        My_Table[i][0] = True
    
    for j in range(1, target + 1): # sets first row of table, checking if nums[0] is less then target
        if nums[0] == j:
            My_Table[0][j] = True
        else:
            My_Table[0][j] = False
    
    
    for i in range(1,len(nums)): # iterates starting at row two considering a different i amount of values
        for j in range(1, target + 1): # goes through each possible value, seeing if it can be reached with the i different elements
            if j >= nums[i]:
                My_Table[i][j] = My_Table[i-1][j] or My_Table[i-1][j-nums[i]]
            else:
                My_Table[i][j] = My_Table[i-1][j]
    # for row in My_Table:
    #     print(row)
    boo = My_Table[len(nums)-1][target] # whether the target can be reached
    
    if boo == False:
        return [[], False]
    i = len(nums) - 1
    
    j = target
    while j != 0: # starting from the last index goes backwards, finds correct results
        res.append(nums[i-1])
        i = i-1 
        j = j - nums[i]
    return[res, True]
def CleverAlgo():
    pass



if __name__ == "__main__":  
    driver()

