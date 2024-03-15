# @Author: Sushant Das

# @Date: 2024-03-15

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to convert a list into a nested dictionary of keys.

# function to create a nested dictionary
def nested_dic(list1,list2,list3):
    nested = {}
    for i in range(len(list1)):
        nested.update({list1[i]:{list2[i]:list3[i]}})
    return (nested)

# main method
def main():
    list1 = ["hello", 'there', 'best']
    list2 = ['friend', 'bye', 'good']
    list3 = [5, 6, 7]
    print("The original lists:",list1,list2,list3)
    print("The nested dictionary:",nested_dic(list1,list2,list3))


if __name__=="__main__":
    main()