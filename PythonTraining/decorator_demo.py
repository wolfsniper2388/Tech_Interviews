# Higher order functions

registry=[]

def register(func):
    'Add a function to a registry'
    name=func.__name__
    registry.append(name)
    return func

def add_docstring(func):
    'A missing docstrings'
    if func.__doc__ is None:
        func.__doc__='<missing doc string>'
    return func

from functools import wraps
def add_logging(func):
    'Create a decorated function with logging behavior'
    @wraps(func)        #copy all the metadata of func to f, to get rid of the copying of __name__ and __doc__
    def f(*args, **kwds):
        print 'Called', func.__name__, 'with', args
        result=func(*args, **kwds)
        print 'Result is', result
        return result
    #f.__name__=func.__name__
    #f.__doc__=func.__doc__
    return f

def cache(func):
    'Decorate a function with caching behavior'
    answers={}
    @wraps(func)
    def f(*args):
        if args in answers:
            return answers[args]
        result = func(*args)
        answers[args] = result
        return result
    return f


# Test code
if __name__=='__main__':
    import time
    
    @register       #the decorator does the exact same thing of 'square=register(square)'
    def square(x):
        'Return a value times itself'
        return x*x
    
    #square=register(square)
    
    @add_docstring
    @register
    @register
    def collatz(x):
        if x%2==0:
            return x//2
        return 3*x+1
    #print 'doc string of collatz',help(collatz)
    #collatz=register(collatz)
    #collatz=register(collatz)
    
    
    @cache
    @register
    def big_calc(x):
        'doing hard work!'
        time.sleep(1)
        result= x+1
        return result
    
    print 'big_calc(x) is', big_calc(5)
    
    
    #big_calc=register(big_calc)
    
    
    #print 'registry is',registry
    
    
    
    # Monkey Patching. To avoid debugging, now all cosine call will have the print
    import math
    orig_cosine=math.cos
    
    def logging_cos(x):
        'Adds print diagnostic messages to cosine'
        print 'Cosine called with',x
        result=orig_cosine(x)
        print 'Result is',result
        return result
    
    math.cos=logging_cos
    
    #print math.cos(3)
    
    
    # Nested scopes
    # Closures happen when you have a function inside a function. The inner function memorizes the variables from nested function above
    
    def f(x):
        y=x+1
        def g(z):
            return z+y
        return g
    
    h=f(5)
    print 'h (20) is',h(20)     # the local variable y is stored at h.__closure__[0].cell_contents
    
    
    def make_adder(x):
        def f(y):
            return x+y
        return f
    
    add_two, add_three = map(make_adder, [2,3])
    
    print 'add_two(10) is',add_two(10)
    print 'add_three(10)',add_three(10)
    
    import math
    
    print 'math log after add_logging'
    print math.log(10)
