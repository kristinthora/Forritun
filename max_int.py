#Takes inputs from user. 
#First input becomes maximum integer. 
#Next input is compared to maximum integer. 
#If it is larger becomes new maximum integer.
#When a negative number is input the program prints maximum integer.
num_int=int(input("Input a number: "))
max_int=num_int
while num_int>=0:
    if num_int>max_int:
        max_int=num_int
    num_int=int(input("Input a number: "))
print("The maximum is",max_int)