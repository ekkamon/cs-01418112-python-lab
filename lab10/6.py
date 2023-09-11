def remove_duplicates(t):
    new_data = []
    
    for val in t:
        if val in new_data:
            continue
        
        new_data.append(val)
        
    return new_data