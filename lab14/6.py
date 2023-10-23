def get_inputs():
    labs = sum([int(val) for val in str(input()).split(' ')])
    grades = [float(val) for val in str(input()).split(' ')]
    users = []
    
    # enter labs
    for _ in range(int(input())):
        data = str(input()).split(' ')
        
        enters = [val for val in data if int(val) == 1]
        classes = len(data)
        
        users.append([(len(enters) / classes) * 100])
        
    # success labs
    for idx in range(len(users)):
        finish_lab = sum([int(val) for val in str(input()).split(' ')])
        users[idx].append((finish_lab / labs) * 100)
        
    return grades, users

def get_failure_users(grades, users):
    passes_class, passes_lab = grades
    
    return [uid for uid in range(len(users)) if users[uid][0] < passes_class and users[uid][1] < passes_lab]

def main():
    grades, users = get_inputs()
    failure = get_failure_users(grades, users)
    
    print(len(failure))
    
    for uid in range(len(users)):
        grade_class, grade_lab = users[uid]
        
        if uid in failure:
            uid = f'({uid + 1})'
        else:
            uid = uid + 1
        
        print(uid, f'{grade_class:.2f}', f'{grade_lab:.2f}')

main()