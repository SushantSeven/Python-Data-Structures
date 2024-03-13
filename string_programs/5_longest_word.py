# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python function that takes a list of words and returns the length of the longest one.

# function to return the longest string in the list
def longest(string_list):
    index_list = []
    for i in string_list:
        index_list.append(len(i))
    return string_list[index_list.index(max(index_list))]

# main method
def main():
    string_list = input("Enter the words as comma seperated values: ").split(" ")
    print(longest(string_list))

if __name__ == "__main__":
    main()