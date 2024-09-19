num = int(input("Ingresa un número: "))

def foo_bar_check(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FooBar"
    elif n % 3 == 0:
        return "Foo"
    elif n % 5 == 0:
        return "Bar"
    else:
        return str(n)

res = foo_bar_check(num)
print(res)