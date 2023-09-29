test_case = str(input())
pass_case = str(input())

test_case = test_case[1:-1]

def is_pass(target):    
    for i in range(len(pass_case)):
        _pass = pass_case[i]

        if target == _pass:
            return True
        
    return False

def get_score():
    score = 0

    for i in range(len(test_case)):
        val = test_case[i]

        if (is_pass(val)):
            score += 1

    return score

score = get_score()
max_score = len(test_case)

print(score)
print(f'{(score / max_score) * 100:.2f}' if max_score > 0 else f'{0:.2f}')