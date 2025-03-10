def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    no_dsign = d.replace("$", "")
    return float(no_dsign)


def percent_to_float(p):
    change_percent = p.replace("%", "")
    p_converted = float(change_percent) / 100
    return p_converted


main()
