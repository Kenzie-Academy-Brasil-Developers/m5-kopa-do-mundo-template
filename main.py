cup_years = []
for year in list(range(2023)):
    if year > 1299 and year%4 == 0:
        print(year)
        cup_years.append(year)
print(cup_years)