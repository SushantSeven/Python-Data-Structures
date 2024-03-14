# @Author: sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to convert a list to a tuple.

# method to convert a list into tuple
def list_to_tuple(items):   
   return tuple(items)
        
# main method
def main():
    ls = [1,2,"Red",True,1,"Red",4,5]
    print("The original list: ",ls)
    print(list_to_tuple(ls))
    print(type(list_to_tuple([1,2,"Red",True,1,"Red",4,5])))
        

if __name__=="__main__":
    main()