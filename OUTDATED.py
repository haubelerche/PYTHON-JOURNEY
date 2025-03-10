#split date by /
# check if month is in bw 1 and 12 and day bt 1 and 31
#split the date by space
#find the number of the month
#rm comma from day variable
#if month/day is less than 10, add a 0
#print the result
def main():
    months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

while True:
    date = input("Date: ")
    try:
        month, day, year = date.split("/")
        month = int(month.replace(" ", ""))
        day = int(day)
        year = int(year.replace(" ", ""))
        if (int(month) > 0 and int(month) < 13) and (int(day) > 0 and int(day) < 32):
            print(year, f"{month:02}", f"{day:02}", sep="-")
            break
    except:
        try:
            if "," not in date:
                raise SyntaxError
            else:
                month, day, year = date.split(" ")
                day = day.replace(",", "")
                day = int(day)
                year = int(year)
                if month in months_list and (int(day) > 0 and int(day) < 32):
                    month = (months_list.index(month)+1)
                    print(year, f"{month:02}", f"{day:02}", sep="-")
                    break
        except:
            pass

main()











