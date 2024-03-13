# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python function that takes two lists and returns True if they have at least one common member.

# method to check common member
def compare_list(list1,list2):
    for item in list1:
        if item in list2:
            return True
    return False

# main method
def main():
    print(compare_list([5,7,10,11],[1,22,3,4,2,6,7,9,0] ))

if __name__ == "__main__":
    main()