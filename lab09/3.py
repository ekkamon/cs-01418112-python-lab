def nb_year(p0, percent, aug, p):
    day = 0
    growth_rate = int(p0)
    total = 0

    while total < p:
        total = int(growth_rate + (growth_rate * (percent / 100) + aug))
        growth_rate = total
        day += 1

    return day


print( nb_year(1000, 2, 0, 200_000) )
print( nb_year(1000, 2, 30, 1150) )
print( nb_year(1500000, 0.25, 1000, 2000000) )





