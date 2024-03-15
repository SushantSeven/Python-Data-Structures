# @Author: Sushant Das

# @Date: 2024-03-15

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

# function to generate a dictionary
def generate(num):
    dct = {}
    for i in range(1,num+1):
        dct.update({i:i*i})
    return dct
# main method
def main():
    num = 5
    print("Generated dictionary",generate(num))


if __name__=="__main__":
    main()