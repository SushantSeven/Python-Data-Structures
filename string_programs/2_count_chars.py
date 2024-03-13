# 2. Write a Python program to count the number of characters (character frequency) in astring.

# function to count the number of occurrence of a character in a string
def count_characters(string, char):
    return string.count(char)

# main function
def main():
    string = input("Enter the string: ")
    char = input("Enter the character to be counted: ")
    print(f"The number of occurrence of {char} in {string} is {count_characters(string,char)} times.")


if __name__ == "__main__":
    main()