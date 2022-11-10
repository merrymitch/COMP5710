def add(a, b):
    return int(a) + int(b) 


def subtract(a, b):
    try: 
        return int(a) - int(b) 
    except ValueError:
        return("Input provided was invalid")
    except:
        return("Something went wrong check inputs")

def multiply(a, b):
    try: 
        return int(a) * int(b)
    except ValueError:
        return("Input provided was invalid")
    except:
        return("Something went wrong check inputs")
    
def divide(a, b):
    try:
        if b == 0:
            return("Cannot divide by zero")
        return int(a) / int (b)
    except ValueError:
        return("Input provided was invalid")
    except:
        return("Something went wrong check inputs")