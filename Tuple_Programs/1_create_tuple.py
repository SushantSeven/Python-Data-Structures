# @Author: sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to create a tuple.

# method to create a tuple
def create_tuple(item1,item2,item3,item4,item5):
    return (item1,item2,item3,item4,item5)

# main method
def main():
    print(create_tuple(1,2,3,4,5))
    print(type(create_tuple(1,2,3,4,5)))
        

if __name__=="__main__":
    main()