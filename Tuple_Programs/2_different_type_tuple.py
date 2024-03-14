# @Author: sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to create a tuple with different data types.

# method to create a tuple of different datatypes
def create_tuple(item1, item2,item3,item4):
    result = (item1, item2, item3, item4)
    return result

# main method
def main():
    print(create_tuple(1,'Red',2.3,True))
    print(type(create_tuple(1,'Red',2.3,True)))
        

if __name__=="__main__":
    main()