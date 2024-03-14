# @Author: sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to remove an item from a tuple.

# method to remove an item from a tuple
def remove_item(items, element):
    new_tuple = tuple( item for item in items if item != element)
    return new_tuple
        
# main method
def main():
    tup = (1,2,"Blue",True,3,"Red",4,5)
    element = 4
    print("Original Tuple: ",tup)
    print(f"After removing {element} : {remove_item(tup, element)}")
        

if __name__=="__main__":
    main()