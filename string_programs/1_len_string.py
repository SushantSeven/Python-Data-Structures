# 1. Write a Python program to calculate the length of a string.

def length_of_string(string):
    return len(string)

def main():
    string = input("Enter your string: ")
    print("Length of string is:",length_of_string(string))

if __name__ == "__main__":
    main()