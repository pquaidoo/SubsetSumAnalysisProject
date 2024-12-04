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
    list0 = list(range(1, 21))
    print((list0))
    target = 50
    list1 = [1,4,2]
    check = bruteForceAlgo(list0, target)
    print(check)
    list2 = [1,2,3]
    check = DynamicProgramingAlgo(list0, target)
    print(check)
    list3 = [1,2,3,10,4,0]
    check = CleverAlgo(list0, target)
    print(check)

"""
Finds Subset sum in O(2^n) by creating a list of all possible subsets and iterates through list. 
If there is a sum, will return the elements in a list that add up to the target, and True boolean
if not it will return an empty array with a False boolean
Input list: list of integers to check, int: target sum
Output list: [list: sublist that adds up to target, boolean: True if there is a sublist that adds up to sum, False if not]
"""
def bruteForceAlgo(nums:list, target:int ):
    leftSubsets = []
    
    def listOfSubset(index, path):
        if index == len(nums):
            leftSubsets.append(path)
            return
        
        listOfSubset(index + 1, path + [nums[index]])
        
        listOfSubset(index + 1, path)
    
    listOfSubset(0, [])

    for i in leftSubsets:
        if sum(i) == target:
            return [i,True]

    return [[],False]
 

def DynamicProgramingAlgo(nums:list, target:int ):
    My_Table = [[False] * (target + 1) for _ in range(len(nums))] # creates a 2d array with false in each index
    res = [] # is the leftSubsets
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
    for row in My_Table:
        print("".join(['T' if cell else 'F' for cell in row]))
    boo = My_Table[len(nums)-1][target] # whether the target can be reached
    if boo == False:
        return [[], False]
    i = len(nums) - 1
    
    j = target
    while i > 0 and j > 0: # starting from the last index goes backwards, finds correct results
        if My_Table[i][j] and not My_Table[i-1][j] :#in the 2d array checks the current indeces and the indeces directly above
            res.append(nums[i]) 
            j -= nums[i]
        i -= 1
    if j > 0 and nums[0] == j: #if index is at the last row it cant check above it so we only need to check if there is still something to subtract form j or out remaining sum. adds the last row if so.
        res.append(nums[0])
        
    
    return[res, True]

def CleverAlgo(nums:list, target:int):
    boo = False
    split = len(nums) // 2

    left = nums[:split]
    right = nums[split:]

    leftTable = dict()
    rightTable = dict()

    correctSubset = []
    
    def leftOfSubset(index, path):
        
        if correctSubset:
            return
        if index == len(left):
            # print(sum(path))
            if sum(path) == target:
                correctSubset.append(path)
                return

            elif sum(path) < target:
                leftTable[sum(path)] = path
                return
        
            return
        
        
        leftOfSubset(index + 1, path + [left[index]])

        leftOfSubset(index + 1, path)
        
    leftOfSubset(0, [])
    if correctSubset:
        return [correctSubset[0], True]
    def rightOfSubset(index, path):
        
        if correctSubset:
            return
        if index == len(right):
            if sum(path) == target:
                correctSubset.append(path)
                return

            elif sum(path) < target:
                rightTable[sum(path)] = path
                return
        
            return
        
        
        rightOfSubset(index + 1, path + [right[index]])
        
        rightOfSubset(index + 1, path)
    
    rightOfSubset(0, [])
    
    if correctSubset:
        return [correctSubset[0], True]
    sortedWeights = list(rightTable.keys())
    sortedWeights.sort()
    leftWeights = list(leftTable.keys())
    for i in range(len(leftWeights)):
        j = 0
        while j < len(sortedWeights):
            if leftWeights[i] + sortedWeights[j] == target:
                correctSubset = leftTable[leftWeights[i]] + rightTable[sortedWeights[j]]
                return [correctSubset, True]
            if (leftWeights[i] + sortedWeights[j]) > target:
                j = len(sortedWeights)
            j += 1
    
    return [correctSubset, boo]


if __name__ == "__main__":  
    driver()

