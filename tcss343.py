import random
import time

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
    
    t = 0
    subsets = [] 
    test1 = []

    n = 6
    r = 1000
    v = True


    for i in range(n):    
        num = random.randint(1, r)
        test1.append(num)
    
    def listOfSubset(index, path):
        if index == len(test1):
            subsets.append(path[:])  # Append a copy of the current path to subsets
            return
        
        # Include the current element
        path.append(test1[index])
        listOfSubset(index + 1, path)
        path.pop()  # Backtrack to remove the element

        # Exclude the current element
        listOfSubset(index + 1, path)

    if not v:
        t = random.randint(sum(test1), sum(test1)*2)
    else:
        randNum = random.randint(1,n)
        for i in range(randNum):
            randomIndex = random.randint(1,len(test1)-1)
            t += test1[randomIndex]
    print(test1, "t=", t,"n=", n, "r=", r )
#######################################################################################################
    #Tests algorithms, prints runtime and outputs 
    start_time = time.perf_counter() 

    #check = bruteForceAlgo(test1, t)

    end_time = time.perf_counter()    # End time in seconds
    execution_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
    print("brute force:"f"Execution time: {execution_time_ms:.2f} ms")
    # print(check)
#######################################################################################################   
    start_time = time.perf_counter() 

    check = DynamicProgramingAlgo(test1, t)

    end_time = time.perf_counter()    # End time in seconds
    execution_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
    print("DP:"f"Execution time: {execution_time_ms:.2f} ms")
    # print(check)
#######################################################################################################
    start_time = time.perf_counter() 

    #check = CleverAlgo(test1, t)

    end_time = time.perf_counter()    # End time in seconds
    execution_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
    print("Clever:"f"Execution time: {execution_time_ms:.2f} ms")
    # print(check)
########################################################################################################

    
"""
Finds Subset sum in O(2^n) by creating a list of all possible subsets and iterates through list. 
If there is a sum, will return the elements in a list that add up to the target, and True boolean
if not it will return an empty array with a False boolean

Input list: list of integers to check, int: target sum
Output list: [list: sublist that adds up to target, boolean: True if there is a sublist that adds up to sum, False if not]
"""
def bruteForceAlgo(nums:list, target:int ):
    subsets = []
    """
    Recursive function to generate all subsets of `nums`.

    index represents the index in the 'left' list. 
     path represents the subset that is being analysed.
    """
    def listOfSubset(index, path): 
        if index == len(nums):
            subsets.append(path)
            return
        
        listOfSubset(index + 1, path + [nums[index]]) # Recursive call if the current subset is added.
        
        listOfSubset(index + 1, path) # Recursive call if subset is not used.
    
    listOfSubset(0, [])

    # Iterates through subsets in 'leftSubsets'
    for i in subsets:
        if sum(i) == target: # Checks if the sum of the current subset equals the target.
            return [i,True] # If subsets match the target sum, returns subset and 'True'.

    return [[],False] # If no subset matches the target sum, return an empty list and `False`.
 
"""
The DynamicProgramingAlgo checks if a subset of `nums` adds up to `target` and to find that subset if it exists.
The algorithm builds a 2D array to track possible sums using elements of `nums`.
It uses this table to decide if the target sum is achievable. If it is, the subset 
is found by backtracking through the array, adding elements that contribute to the sum.

Input list: list of integers to check, int: target sum
Output list: [list: sublist that adds up to target, boolean: True if there is a sublist that adds up to sum, False if not]
"""
def DynamicProgramingAlgo(nums:list, target:int ):
    # start_time = time.time() 
    

    My_Table = [[False] * (target + 1) for _ in range(len(nums))] # Creates a 2d array, initially with false in each index.
    res = [] # is the leftSubsets
    for i in range(len(nums)): # Makes first column all true.
        My_Table[i][0] = True
    
    for j in range(1, target + 1): # Sets first row of table, checking if nums[0] is less then target
        if nums[0] == j:
            My_Table[0][j] = True # If `nums[0]` equals `j`, set the cell to `True`.
        else:
            My_Table[0][j] = False # Else `False`.
    
    # end_time = time.time()    # End time in seconds
    # execution_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
    # print("1. Instantiateing: "f"Execution time: {execution_time_ms:.2f} ms")


    # start_time = time.time() 
    for i in range(1,len(nums)): # Iterates starting at row two considering a different i amount of values
        for j in range(1, target + 1): # Goes through each possible value, seeing if it can be reached with the i different elements
            if j >= nums[i]:
                My_Table[i][j] = My_Table[i-1][j] or My_Table[i-1][j-nums[i]]
            else:
                # If `nums[i]` is greater than the current target `j`, it is not included.
                My_Table[i][j] = My_Table[i-1][j]

    # for row in My_Table: # Prints visual for debugging.
    #     print("".join(['T' if cell else 'F' for cell in row]))

    boo = My_Table[len(nums)-1][target] # Checks whether the target can be reached by the last array.


    # end_time = time.time()    # End time in seconds
    # execution_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
    # print("2. Find initial boolean: "f"Execution time: {execution_time_ms:.2f} ms")

    if boo == False:
        # If target is not applicable, returns empty list and 'False'.
        return [[], False]
    
    i = len(nums) - 1
   
    j = target
    # start_time = time.time() 

    while i > 0 and j > 0: # Starting from the last index goes backwards, finds correct results.
        if My_Table[i][j] and not My_Table[i-1][j] :# In the 2d array checks the current indeces and the indeces directly above.
            res.append(nums[i]) 
            j -= nums[i]
        i -= 1
    if j > 0 and nums[0] == j: # If index is at the last row it cant check above it so we only need to check if there is still something to subtract form j or out remaining sum. Adds the last row if so.
        res.append(nums[0])
        
    # end_time = time.time()    # End time in seconds
    # execution_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
    # print("3. backTracking:"f"Execution time: {execution_time_ms:.2f} ms")

    return[res, True] # Returns the subset and `True` when target has been reached.

"""
The CleverAlgo finds if a subset of `nums` adds up to `target` and to find that subset if it exists.
The algorithm uses the divide-and-conquore strategy and explores all subsets of each half recursively.
It stores all possible subset sums in hash tables. If no exact match is found
in one half, it combines subset sums from both halves to check if they add up to `target`.

Input list: list of integers to check, int: target sum
Output list: [list: sublist that adds up to target, boolean: True if there is a sublist that adds up to sum, False if not]
"""
def CleverAlgo(nums:list, target:int):
    boo = False
    split = len(nums) // 2

    left = nums[:split] 
    right = nums[split:]

    leftTable = dict()
    rightTable = dict()

    correctSubset = []
    """
     Recursively generates subsets of `left` and updates `leftTable` with their sums.
     Updates the `leftTable` with their sums if the sum is less than the target. 
     If a subset equals the target, it is stored in `correctSubset`.
     index represents the index in the 'left' list. 
     path represents the subset that is being analysed.
     """
    def leftOfSubset(index, path):
        
        if correctSubset: # Stops recursion if the target has been found.
            return
        if index == len(left): # Base Case, checks if recursion has reached the end of the 'left' list.
            if sum(path) == target: # If sum of current subset matches target, it then stores it into 'correctSubset'.
                correctSubset.append(path)
                return

            elif sum(path) < target: # If sum of the subset is less than target, it is stored in the 'leftTable'.
                leftTable[sum(path)] = path
                return
        
            return
        
        
        leftOfSubset(index + 1, path + [left[index]]) # Recursive call if the current subset is added.

        leftOfSubset(index + 1, path) # Recursive call if subset is not used.
        
    leftOfSubset(0, [])
    if correctSubset: # If target is satisfied, returns the correctSubset along with 'true'.
        return [correctSubset[0], True]
    
    """
     Recursively generates subsets of `right` and updates `rightTable` with their sums.
     Updates the `rightTable` with their sums if the sum is less than the target. 
     If a subset equals the target, it is stored in `correctSubset`.
     index represents the index in the 'left' list. 
     path represents the subset that is being analysed.
     """
    def rightOfSubset(index, path):
        
        if correctSubset: # Stops recursion if the target has been found.
            return
        if index == len(right): # Base Case, checks if recursion has reached the end of the 'left' list.
            if sum(path) == target: # If sum of current subset matches target, it then stores it into 'correctSubset'.
                correctSubset.append(path)
                return

            elif sum(path) < target: # If sum of the subset is less than target, it is stored in the 'rightTable'.
                rightTable[sum(path)] = path
                return
        
            return
        
        
        rightOfSubset(index + 1, path + [right[index]]) # Recursive call if the current subset is added.
        
        rightOfSubset(index + 1, path) # Recursive call if subset is not used.
    
    rightOfSubset(0, [])
    
    if correctSubset: # If target is satisfied, returns the correctSubset along with 'true'.
        return [correctSubset[0], True]
    
    sortedWeights = list(rightTable.keys()) # Stores subset sums from 'rightTable'.
    sortedWeights.sort() # Sorts the subset sums in ascending order from the 'rightTable' list.
    leftWeights = list(leftTable.keys()) # Stores subset sums from 'leftTable' as a list.

    for i in range(len(leftWeights)): # Iterates through each subset sum in 'leftWeights'.
        j = 0
        # Use a while loop to compare sums from `leftWeights` and `sortedWeights`.
        while j < len(sortedWeights):
            # Check if the sum of the current subset sums equals the target.
            if leftWeights[i] + sortedWeights[j] == target: 
                # If the target is matched, combine the subsets from `leftTable` and `rightTable`.
                correctSubset = leftTable[leftWeights[i]] + rightTable[sortedWeights[j]]
                # Returns if the combined subset is true and a 'True' boolean.
                return [correctSubset, True]
            # If combined sum is over target, breaks out of loop.
            if (leftWeights[i] + sortedWeights[j]) > target:
                j = len(sortedWeights)
            j += 1
    
    return [correctSubset, boo] 


if __name__ == "__main__":  
    driver()

