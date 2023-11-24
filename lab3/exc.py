# import time
#
# def timer(sec):
#     start = time.time()
#     for i in range(sec):
#         print(time.strftime("%H : %M : %S", time.localtime()))
#         time.sleep(1)
#     end = time.time()
#     time_taken = int(end) - int(start)
#     print("Program zajął: " + str(time_taken) + " sekund")
#
#
# timer(5)
#
uczestnicy = ["Anna", "Piotr", "Katarzyna", "Marek", "Joanna"]
with open("names.txt", "w") as file:
    for uczestnik in uczestnicy:
        file.write(f"{uczestnik},{len(uczestnik)}\n")

with open("names.txt", "r") as file:
    lines = file.readlines()

imiona = []
liczba_liter = []

for line in lines:
    imie, liczba = line.strip().split(',')
    imiona.append(imie)
    liczba_liter.append(int(liczba))

print("Imiona:", imiona)
print("Liczba liter:", liczba_liter)

