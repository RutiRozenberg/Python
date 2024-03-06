from datetime import datetime
from functools import wraps

#סיבוכיות
def time(func):
    @wraps(func)
    def wrapper(*args , **kwargs):
        start = datetime.now()
        func(*args , **kwargs)
        print(datetime.now()-start)
    return wrapper

@time
def print_n_numbers(n):
    for i in range(n):
        print(i)

#זיכרון מטמון
def cache(func):
    @wraps(func)
    def wrapper(*args ,**kwargs):
         if func.__name__ not in allFunc:
             allFunc.update({func.__name__:{args[0]: func(*args, **kwargs)}})
         elif args[0] not in allFunc[func.__name__]:
             allFunc[func.__name__].update({args[0]: func(*args, **kwargs)})
         return allFunc[func.__name__][args[0]]
    return wrapper


@cache
def fib(n):
    x=[]
    i=0
    a=0
    b=1
    while i<n:
        x.append(a)
        i +=1
        c=a+b
        a=b
        b=c
    return x


@cache
def gg(m):
    return m+2
#הפעלת הפונקציות
if __name__ == '__main__':
    print_n_numbers(10)
    print_n_numbers(100)
    allFunc = {}
    print(fib(10))
    print(fib(10))
    print(fib(5))
    gg(45)
    # print(allFunc)



