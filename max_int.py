num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
# Fill in the missing code ererger
while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))
    if num_int < 0:
        print("The maximum is", max_int)    # Do not change this line
