
call = 0
def counter_manager(func):
    def proxy(*args,**kwargs):
        global call
        call += 1
        print(call)
        return func(*args, **kwargs)
    return proxy

@counter_manager
def hack(a,b,c):
    print(a + b + c)

hack(1, 2, 3)
hack(4, 5, 6)
