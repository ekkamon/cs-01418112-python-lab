def nb_year(p0, percent, aug, p):
    day = 1
    growth = p0
    total = 0
    
    while True:
        total = (growth + (growth * (percent / 100)) + aug)
        
        if total >= p:
            break
        
        growth = total
        day += 1
        
    return day


print( nb_year(1000, 2, 0, 200_000) )
print( nb_year(1000, 2, 30, 1150) )
print( nb_year(1500000, 0.25, 1000, 2000000) )





