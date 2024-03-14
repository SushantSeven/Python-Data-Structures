# @Author: sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to create the colon of a tuple.

from copy import deepcopy
# method to create a colon of a tuple
def colon(tup):
    tc = deepcopy(tup)
    tc[4].append(50)
    print ("The original tuple: ",tup)
    print(tc)
# main method
def main():
    tup = ("Tutor", 'J', 23 , 56.67 , [23,12] , True) 
    colon(tup)

if __name__=="__main__":
    main()