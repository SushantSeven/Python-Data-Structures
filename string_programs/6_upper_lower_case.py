# method to desiplay upper case and lower case
def upper_lower(string):
    return string.upper(), string.lower()

# main method
def main():
    string = input("Enter a string: ")
    print(*(upper_lower(string)))

if __name__ == "__main__":
    main()