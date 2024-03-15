# @Author: Sushant Das

# @Date: 2024-03-15

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to count the values associated with key in a dictionary.

# function to count the values associated to a key
def count_value(dct):
    count = 0
    for d in dct:
        if d["success"]:
            count+=1
    return count
# main method
def main():
    dct = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':True, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    print("The original dictionary:",dct)
    print("Number of values whose success is True:",count_value(dct))


if __name__=="__main__":
    main()