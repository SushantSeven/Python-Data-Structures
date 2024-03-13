# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to reverse a string.

# method to reverse a string
def reverse_string(string):
    return string[::-1]

# main method
def main():
    string = input("Enter a string: ")
    print(reverse_string(string))

if __name__ == "__main__":
    main()