import datetime

print("Podaj imię")
name = input()
print("Podaj wiek")
age = int(input())

print("Cześć " + name +
      "\nTwoje imię ma: " + str(len(name)) +
      " liter i zaczyna się od: " + name[0] +
      "\nTeraz masz " + str(age) + " lat, a za rok będzie to: " +
      str(age + 1) + " lat. Twój rok urodzenia to: " + str(datetime.date.today().year - age))