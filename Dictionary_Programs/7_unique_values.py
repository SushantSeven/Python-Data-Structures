# @Author: Sushant Das

# @Date: 2024-03-15

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to print all unique values in a dictionary.

# function to print unique values in dictionary
def unique_values(dct):
    new_dct = set()
    for value in dct:
        for val in value.values():
            new_dct.add(val)
    return (new_dct)
    
# main method
def main():
    dct = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    print("The original dictionary:",dct)
    print("The unique values: ",unique_values(dct))


if __name__=="__main__":
    main()