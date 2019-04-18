# Module 2
#   Programming Assignment 2
#     Prob-3.py

# Nathan Spelts

def example():
    print("\nExample Output")

    # print a blank line
    print()

    # create three variables and assign three values in a single statement
    v1, v2, v3 = 21, 12.34, "hello"

    # print the variables
    print("v1:", v1)
    print("v2:", v2)
    print("v3:", v3)

def studentCode():
    # replace <name> with your name
    print("\nNathan's Output")
    
    # print a blank line
    print()

    # replicate the assignment statement above, but use your own variable
    # names and values
    myv1, myv2, myv3 = 3.14, 6485, "CTEC 121"
    # print the values of the 3 variables
    print("myv1:", myv1)
    print("myv2:", myv2)
    print("myv3:", myv3)
    # Get 3 values from the user and assign them to the variables defined
    # above. See the page in Canvas on Simulataneous Assignment
    # BONUS POINTS for using the split() method

    print()
    myv1, myv2, myv3 = eval(input("Enter 3 values seperated by commas: "))
    print("myv1:", myv1)
    print("myv2:", myv2)
    print("myv3:", myv3)
example()
studentCode()

