# method to add ing or ly at the end of a string
def add_ing_ly(string):
    if len(string) >= 3:
        if string.endswith("ing"):
            return string+"ly"
        else:
            return string+"ing"
    else:
        return string

# main method
def main():
    string = input("Enter the string: ")
    print(add_ing_ly(string))

if __name__ == "__main__":
    main()