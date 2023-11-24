import math
def variables():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    return a, b, c

def square(a, b, c):
    d = (b**2) - (4*a*c)

    if d < 0:
        return None
    elif d == 0:
        x = (-b) / (2 * a)
        return x
    else:
        x1 = round((-b - math.sqrt(d)) / (2 * a),2)
        x2 = round((-b + math.sqrt(d)) / (2 * a),2)
        return x1, x2

def heron(a, b, c):
    if a > 0 and b > 0 and c > 0 and((a+b) > c) and ((a+c) > b) and ((c+b) > a):
        p = (a+b+c)/2
        s = math.sqrt(p * (p-a) * (p-b) * (p-c))
        return s
    else:
        return None

choice = input("[1] # Równanie Kwadratowe # \n[2] # Wzór Herona # \n... ")

match choice:
    case "1":
        a, b, c = variables()
        print(square(a, b, c))
    case "2":
        a, b, c = variables()
        print(heron(a, b, c))
    case _:
        print("Błędne dane")