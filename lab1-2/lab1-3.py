def tax(annual_income):
    if annual_income <= 85528:
        tax = annual_income * 0.12
    else:
        tax = 85528 * 0.12 + (annual_income - 85528) * 0.32

    return tax

def month_to_year(monthly_income):
    return monthly_income * 12

print(">>> Wybierz dochód <<<")
income_type = input("Wpisz 'miesięczny' lub 'roczny': ").lower()

if income_type == "miesięczny":
    monthly_income = float(input("Podaj dochód miesięczny: "))
    annual_income = month_to_year(monthly_income)
else:
    annual_income = float(input("Podaj dochód roczny: "))

print(f"Twój roczny dochód wynosi {annual_income} PLN.")
print(f"Podatek dochodowy wynosi {tax(annual_income)} PLN.")