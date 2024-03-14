# @Author: sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to check whether an element exists within a tuple.

# method to find if an element if present in a tuple or not
def present_or_not(items, element):
    
   return "Present" if element in items else "Not present"
        
# main method
def main():
    tup = (1,2,"Red",True,1,"Red",4,5)
    element = 2
    print("The tuple is: ",tup)
    print(f"{element} is {present_or_not(tup,element)}")
        

if __name__=="__main__":
    main()