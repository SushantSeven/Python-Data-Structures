# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to count occurrences of a substring in a string.

# function to check the occurrence of  a substring 
def occur(string, sub_string):
    return (string.count(sub_string))

# main method
def main():
    string = input("Enter the string: ")
    sub_string = input("Enter the sub string: ")
    print(f"{occur(string, sub_string)} times")

if __name__=="__main__":
    main()