def function_with_uncommon_bug(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input types")
        return None
    else:
        return result

#This function does not handle the potential OverflowError.  It will be triggered by the function if the values of a and b are too big, resulting in an integer overflow.