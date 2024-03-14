# @Author: sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to unpack a tuple in several variables.

# method to unpack a tuple
def unpack_tuple(items):
    print ("Unpackt items: ",*items)

# main method
def main():
    tup = (1,2,"Red", True)
    print(f"Original tupple: {tup}")
    unpack_tuple(tup)
        

if __name__=="__main__":
    main()