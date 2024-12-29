import sys
def function_with_solution(a, b):
    try:
        if abs(a) > sys.maxsize or abs(b) > sys.maxsize:
            print("Warning: potential overflow detected. Using decimal module.")
            from decimal import Decimal
            a = Decimal(str(a))
            b = Decimal(str(b))
            result = a / b
        else:
            result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except OverflowError:
        print("Error: Integer overflow detected during division.")
        return None
    except TypeError:
        print("Error: Invalid input types")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    else:
        return result