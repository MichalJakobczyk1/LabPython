print("Podaj wiek")
age = int(input())
print("Podaj stan konta")
money = int(input())
missing_age = 18 - age
missing_money = 20 - money

if age < 18 and money < 20:
    print("masz za mało pieniędzy i jesteś za młody, brakuje ci: "+ str(missing_age) + "lat i: " + str(missing_money) + "zł")
elif age < 18:
    print("jesteś za młody, brakuje ci: " + str(missing_age))
elif money < 20:
    print("masz za mało pieniędzy, brakuje ci: " + str(missing_money))
else:
    print("jesteś pełnoletni i masz wystarczającą ilośc pieniędzy")
