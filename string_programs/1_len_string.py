# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to calculate the length of a string.

# function to check length of a string
def length_of_string(string):
    return len(string)

# main method
def main():
    string = input("Enter your string: ")
    print("Length of string is:",length_of_string(string))


if __name__ == "__main__":
    main()