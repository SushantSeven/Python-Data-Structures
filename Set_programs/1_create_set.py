# @Author: Sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to create a set.

# function create a set
def create_set(item1,item2,item3,item4):
    temp = [item1,item2,item3,item4]
    return set(temp)

# main method
def main():
    item1 = 1
    item2 = 2
    item3 = 3
    item4 = 2
    print(create_set(item1,item2,item3,item4))
    print(type(create_set(item1,item2,item3,item4)))

if __name__ == "__main__":
    main()