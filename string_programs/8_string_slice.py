# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to get the last part of a string before a specified character.

# method to slice the given string
def slice_string(string, character):
    return string[:string.index(character)]

# main method
def main():
    string = input("Enetr a string: ")
    character = input("Enter the seperator: ")
    print(slice_string(string, character))

if __name__ == "__main__":
    main()