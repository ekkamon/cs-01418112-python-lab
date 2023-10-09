def count_factors_3_7(ls):
    return len([val for val in ls if val % 3 == 0 or val % 7 == 0])

def filter_factors_3_7(ls):
    first, second = [], []

    for val in ls:
        if val < 1:
            continue
        
        if val % 3 == 0 or val % 7 == 0:
            first.append(val)
        else:
            second.append(val)

    return [first, second]