# @Author: Sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a python program to check whether two lists are circularly identical.

# method to append one list to another
def circular(list1, list2):
    flag = False
    if len(list1) == len(list2):
        for i in list1:
            if list1.count(i) == list2.count(i):
                flag = True
            else:
                return False
        return flag

    else:
        return flag

# main method
def main():
    list1 = [10, 10, 10, 0, 0]
    list2 = [1, 10, 10, 0, 0]
    print(f"The original lists are: {list1} {list2}")
    print(f"circularly identical: {circular(list1,list2)}")


if __name__ == "__main__":
    main()