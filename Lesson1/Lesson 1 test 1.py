print("Введите год")
year = int (input())
if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print("Year", year, "Visokosnyi")
else:
    print("Year", year, "not visakosnyi")
