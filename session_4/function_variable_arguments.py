# arbitrary number of arguments
# This function receives a tuple of arguments - tuple items can be accessed

def function_variable_arguments(*kids):
    print("The youngest child is " + kids[2])

function_variable_arguments("Joe", "Luke", "Sean")