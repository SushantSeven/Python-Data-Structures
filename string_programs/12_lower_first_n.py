# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to lowercase first n characters in a string.

# method to lower first n characters of a string
def lower_n(string, n):
    begin = (string[:n]).lower()
    end = string[n:]
    return begin+end

# main method
def main():
    string = input("Enter the string: ")
    n = int(input("Enter the first n number of characters: "))
    print(lower_n(string, n))

if __name__=="__main__":
    main()