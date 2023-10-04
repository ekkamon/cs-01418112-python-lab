def filter_sort_factors_3_7(ls):
    first = [val for val in ls if val % 3 == 0 or val % 7 == 0]
    second = [val for val in ls if val % 3 > 0 and val % 7 > 0]
    
    first.sort()
    second.sort(reverse = True)
    
    return [first, second]

print(filter_sort_factors_3_7([7, 5, 3, 2, 1, 10]))