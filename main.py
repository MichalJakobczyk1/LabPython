# isOlder = input("ile masz lat?")
# if int(isOlder) >= 18:
#     print("jesteś pełnoletni")
# else:
#     print("jesteś za młody")

# names = ["Asia","Basia","Kasia","Joasia"]
# print(sorted(names))
# names.reverse()
# print(names)
# names.append("Jan")
# print(names)

# dict = { "jabłko": 5,"banan": 10,"pomarańcza": 8 }
# print(sum(dict.values()))

# names = ["Asia","Basia","Kasia","Joasia"]
# for name in names:
#     print(name)
#
# numbers = [1,5,10,15,20]
# for number in numbers:
#     print(number*number)

# value = 0
# while value < 1000:
#     print(value)
#     value += 5
#     if(value == 1000):
#         print(value)
#         break

# for i in range(0,101):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     else:
#         print(i*i)

# def rect(a,b):
#     print(a*b)
#
# rect(2,3)

# def bmi_calc(weight,height):
#     bmi = weight/(height*height)
#     print(bmi)
#     result = ""
#     if bmi < 18.5:
#         result = "niedowaga"
#     elif bmi > 25:
#         result = "nadwaga"
#     else:
#         result = "waga optymalna"
#
#     return result
#
# a = bmi_calc(78,1.82)
# print("moje bmi to: " + str(a))

# def fun(first,second, *others):
#     print([first, second] + list(others))
#
# fun(1,2)
# fun(1,2,3,4)