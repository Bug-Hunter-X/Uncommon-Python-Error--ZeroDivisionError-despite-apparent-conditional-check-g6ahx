def function_with_uncommon_error_fixed(a, b):
    if b == 0:
        return 0 #Handle b being 0 to avoid ZeroDivisionError
    elif a == 0:
        return 0 # Handle a being 0 to avoid ZeroDivisionError
    else:
        return a / b

result = function_with_uncommon_error_fixed(0, 5) 