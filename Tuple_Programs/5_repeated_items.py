# @Author: sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to find the repeated items of a tuple.

# method to find repeated items in a tuple
def repeated(items):
    result = []
    for item in items:
        if items.count(item)>1 and item not in result:
            result.append(item)
    return tuple(result)

# main method
def main():
    tup = (1,2,"Red",True,1,"Red",4,5)
    print(f"Original tuple is: {tup}")
    print("Repeated items: ",repeated(tup))
        

if __name__=="__main__":
    main()