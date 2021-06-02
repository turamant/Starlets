def wrapper_html(func):
    def function(*args, **kwargs):
        resultat = func(*args, **kwargs)
        return f"<h2>Результат: {resultat}</h2>"
    return function



def wrapper(func):
    '''Decorator'''
    def function(*args, **kwargs):
        print("Имя декорируемой функции", func.__name__)
        print("были переданы аргументы: ", *args, **kwargs)
        resultat = func(*args, **kwargs)
        return resultat
    return function

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

@wrapper_html
@wrapper
def add(x, y):
    return x + y

@wrapper
@wrapper_html
def mul(x, y):
    return x * y

z = add(1,3)
z2 = mul(3, 5)
print(z, z2)
