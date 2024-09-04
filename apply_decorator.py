def decorator_func(func):
    """
    A simple decorator that prints a message before calling the original function.
    """
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    """
    This function takes a function as input and applies the decorator 'decorator_func' to it.
    """
    # Apply the decorator to the input function
    return decorator_func(func)