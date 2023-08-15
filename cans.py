import math

def paint(width,height,coverage):
    #width = int(input("Enter the width:"))
    #height = int(input("Enter the width:"))
    number_of_cans = math.ceil((width * height) / coverage)
    print("The number of cans needed is", number_of_cans)
    
#paint(4,6,8) positional arguments
paint(coverage=5,width=2,height=4)  #keyword arguments