# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to count the number of characters (character frequency) in a string.

# function to count the number of occurrence of a character in a string
def count_characters(string):
    new_string = "".join(string)
    result_dic = {}
    for i in string:
        result_dic[i] = new_string.count(i)
    return (result_dic)
    
# main function
def main():
    string = list(input("Enter the string: "))
    print(count_characters(string))
    

if __name__ == "__main__":
    main()