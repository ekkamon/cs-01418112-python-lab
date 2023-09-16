max_score = int(input())
pass_score = float(input())
score_count = int(input())

pass_score_list = []
not_pass_idx = []

for i in range(score_count):
    value = int(input())
    percent = (value / max_score) * 100
    
    pass_score_list.append(percent)
    
    if percent < pass_score:
        not_pass_idx.append(i)
        
print(len(not_pass_idx))

for i in range(len(pass_score_list)):
    student_id = i + 1
    
    txt_student_id = f'({student_id})' if i in not_pass_idx else student_id
    print(txt_student_id, f'{pass_score_list[i]:.2f}')