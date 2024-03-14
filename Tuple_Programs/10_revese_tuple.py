# @Author: sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to reverse a tuple.

# method to slice a tuple
def reverse_tuple(tup):
    new_tup = tuple(tup[i] for i in range(len(tup)-1,-1,-1))
    return new_tup
        
# main method
def main():
    tup = (1,2,"Blue",True,3,"Red",4,5)
    print("The original tuple: ",tup)
    print(f"reversed tuple : {reverse_tuple(tup)}")
    

if __name__=="__main__":
    main()