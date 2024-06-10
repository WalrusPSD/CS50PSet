def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    fixed_dollars = d.replace("$","")
    return float(fixed_dollars)

def percent_to_float(p):
    fixed_percent = float(p.replace("%", ""))
    return fixed_percent / 100

main()
