def cloth_size(width_list):
    sizes = {
        'S': 0,
        'M': 0,
        'L': 0
    }
    
    for size in width_list:
        if size <= 36:
            sizes['S'] += 1
        elif size <= 44:
            sizes['M'] += 1
        else:
            sizes['L'] += 1
            
    return sizes