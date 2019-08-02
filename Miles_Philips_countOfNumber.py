# Miles Philips
# Prog 260
# 8-1-19
# Function to find count of how many times a given number appears in an unsorted list.
import random

#Public function that uses binary search algorithm to find the index
# of the one of the occurances of the given value if it is found, otherwise return -1
def binarySearchRecursive(mylist, value):
    if len(mylist) == 0:
        return -1
    else: 
        midpoint = len(mylist)//2
        if mylist[midpoint] == value:
            return midpoint
        else:
            if value < mylist[midpoint]:
                return binarySearchRecursive(mylist[:midpoint],value)
            else:
                return binarySearchRecursive(mylist[midpoint+1:],value)

    # Non-recursive version
    # index = int(len(mylist)/2) -1
    # end = int(len(mylist)) - 1
    # while mylist[index] != value:
    #     if index == end:
    #         return -1
    #     elif mylist[index] > value:
    #         end = index
    #         index = int(index/2)
    #     elif mylist[index] < value:
    #         index = int((index+1 + end)/2)
    # return index
    
#Private function that uses binary search algorithm to find the index
# of the one of the occurances of the given value if it is found, otherwise return -1
def __binarySearchRecursive(mylist, value, low, high):
    if high-low <= -1:
        return -1
    else:
        midpoint = low + (high - low ) // 2
        if mylist[midpoint] == value:
            return midpoint
        else:
            if value < mylist[midpoint]:
                return __binarySearchRecursive(mylist, value, low, midpoint-1)
            else:
                return __binarySearchRecursive(mylist ,value, midpoint+1, high)

def countOfNumber(mylist, number):
    ''' Function to find count of duplicates of given item in the given unsorted list.
    '''
    # First create a sorted version of mylist
    # call binarySearchRecursive function with the sorted list and number to
    # get the index of the number.
    # Call __countOfNumber - the private function - to count number of
    # occurrences if the number was found, else return 0
    sortedlist = sorted(mylist)
    index = binarySearchRecursive(sortedlist, number)
    return __countOfNumber(sortedlist, number, index)
    
def __countOfNumber(mylistSorted, number, index):
    ''' Function to count number of duplicates of number.
    Assumption: Atleast one occurance of number was found at index
    Need to look on either side of index to count the occurrences of number
    '''
    # This code confuses me & I'm not sure what I'm supposed to do with it. Am I supposed to to add to it? replace it? 
    # assert(mylistSorted[index] == number)
    # return 0   
    
    # I think it should look somethng like this instead
    if index >= len(mylistSorted):
        return 0
    found = mylistSorted[index] == number
    return found + __countOfNumber(mylistSorted, number, (index +1))

def main():
    list1 = [40, 1, 2, 86, 4, 100, 9, 100, 35, 10, 21, 82, 26, 59, 72, 100, 98,
             25, 1, 61, 84, 75, 88, 52, 3, 81, 69, 75, 51, 88, 13, 8, 27, 47, 55,
             16, 15, 57, 85, 75, 99, 23, 59, 90, 69, 53, 32, 54, 42, 65, 87, 63,
             96, 24, 87, 100, 3, 75, 21, 8, 81, 37, 16, 5, 22, 29, 12, 45, 48, 4,
             4, 25, 25, 7, 7, 24, 67, 7, 34, 97, 21, 55, 39, 64, 23, 41, 49, 34, 57, 53,
             13, 35, 86, 23, 3, 51, 3, 78, 5, 46, 89, 91, 73, 35, 48, 99, 85, 80, 11,
             55, 7, 89, 97, 49, 17, 43, 90, 66, 43, 21, 60, 30, 86, 93, 42, 55, 22, 89,
             75, 8, 84, 43, 35, 53, 4, 100, 17, 32, 71, 37, 88, 15, 1, 57, 100, 84,
             40, 17, 57, 6, 35, 97, 74, 29, 5, 66, 42, 43, 34, 26, 94, 75, 72, 22,
             60, 36, 50, 68, 99, 37, 61, 67, 27, 72, 34, 57, 1, 32, 31, 93, 59, 56,
             71, 95, 40, 69, 43, 2, 83, 93, 52, 38, 81, 80, 50, 41, 75, 95, 5, 8, 65, 67]

    print("Welcome to Count of Number Program")

    print("Searching from the unsorted list...")
    print(list1)
    number = 1
    print("Searching ", number)
    print(f"Number {number} appears {countOfNumber(list1,number)} times in the list")
    number = 21
    print("Searching ", number)
    print(f"Number {number} appears {countOfNumber(list1,number)} times in the list")
    number = 92
    print("Searching ", number)
    print(f"Number {number} appears {countOfNumber(list1,number)} times in the list")
    number = 100
    print("Searching ", number)
    print(f"Number {number} appears {countOfNumber(list1,number)} times in the list")

    print("Searching a random number")
    number = random.randint(1,100)
    print(f"Number {number} appears {countOfNumber(list1,number)} times in the list")
    
    
if __name__ == "__main__":
    main()
    
