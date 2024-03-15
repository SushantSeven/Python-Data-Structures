# @Author: Sushant Das

# @Date: 2024-03-15

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to print a dictionary in table format.

# function to print a dictionary in table format
def table_format(dct):
    print("{:<10}{:<10}{:<10}{:<10}".format('Sl.no','Name','Age','Subject'))
    for d in dct.items():
        print("{:<10}{:<10}{:<10}{:<10}".format(d[0],d[1][0],d[1][1],d[1][2]))
# main method
def main():
    dct = {1: ["Samuel", 21, 'Data Structures'],2: ["Richie", 20, 'Machine Learning'],3: ["Lauren", 21, 'OOPS with java'],}
    print("Original dictionary:",dct)
    table_format(dct)


if __name__=="__main__":
    main()