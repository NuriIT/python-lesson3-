# Global variable
global_var =10

def add_variables():
    # Local variable set set initially
    local_var = 5
    # Adding global and local variables the first time
    first_result = global_var + local_var

    # Change the local variable for the second calculation
    local_var = 10
    # Adding global and local variables the second time
    second_result = global_var + local_var

    return first_result, second_result

# Calling the function and printing the results
first, second = add_variables()
print("First result:", first) # Outputs: 25
print("Second result:", second) # Outputs: 30



